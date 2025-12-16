from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key="AIzaS<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Image Generator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background-color: #0a0a0a;
            color: #ffffff;
            min-height: 100vh;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .header h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #ffffff, #888888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            font-size: 1.1rem;
            color: #888888;
            max-width: 600px;
            margin: 0 auto;
        }

        .generator-section {
            background: #111111;
            border: 1px solid #333333;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .input-group {
            margin-bottom: 1.5rem;
        }

        .input-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #cccccc;
        }

        .prompt-input {
            width: 100%;
            padding: 1rem;
            background: #1a1a1a;
            border: 1px solid #333333;
            border-radius: 8px;
            color: #ffffff;
            font-size: 1rem;
            resize: vertical;
            min-height: 120px;
            transition: all 0.3s ease;
        }

        .prompt-input:focus {
            outline: none;
            border-color: #4a9eff;
            box-shadow: 0 0 0 3px rgba(74, 158, 255, 0.1);
        }

        .controls {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .control-group {
            display: flex;
            flex-direction: column;
        }

        .control-group label {
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            color: #cccccc;
        }

        .control-input {
            padding: 0.75rem;
            background: #1a1a1a;
            border: 1px solid #333333;
            border-radius: 6px;
            color: #ffffff;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .control-input:focus {
            outline: none;
            border-color: #4a9eff;
            box-shadow: 0 0 0 2px rgba(74, 158, 255, 0.1);
        }

        .generate-btn {
            width: 100%;
            padding: 1rem 2rem;
            background: #4a9eff;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .generate-btn:hover {
            background: #3a8eef;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(74, 158, 255, 0.3);
        }

        .generate-btn:active {
            transform: translateY(0);
        }

        .generate-btn:disabled {
            background: #333333;
            color: #666666;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .loading-spinner {
            display: none;
            width: 20px;
            height: 20px;
            border: 2px solid #ffffff40;
            border-top: 2px solid #ffffff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-right: 0.5rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .results-section {
            background: #111111;
            border: 1px solid #333333;
            border-radius: 12px;
            padding: 2rem;
            min-height: 400px;
        }

        .results-header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .results-header h2 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: #ffffff;
        }

        .placeholder {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 300px;
            color: #666666;
            text-align: center;
        }

        .placeholder-icon {
            width: 64px;
            height: 64px;
            margin-bottom: 1rem;
            opacity: 0.3;
        }

        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .image-card {
            background: #1a1a1a;
            border: 1px solid #333333;
            border-radius: 8px;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .image-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }

        .image-placeholder {
            width: 100%;
            height: 300px;
            background: #222222;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666666;
            font-size: 0.9rem;
        }

        .image-info {
            padding: 1rem;
        }

        .image-prompt {
            font-size: 0.9rem;
            color: #cccccc;
            margin-bottom: 0.5rem;
            line-height: 1.4;
        }

        .image-details {
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: #888888;
        }

        .status-message {
            text-align: center;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 6px;
            font-size: 0.9rem;
        }

        .status-success {
            background: rgba(34, 197, 94, 0.1);
            color: #22c55e;
            border: 1px solid rgba(34, 197, 94, 0.2);
        }

        .status-error {
            background: rgba(239, 68, 68, 0.1);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.2);
        }

        .status-info {
            background: rgba(74, 158, 255, 0.1);
            color: #4a9eff;
            border: 1px solid rgba(74, 158, 255, 0.2);
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }

            .header h1 {
                font-size: 2rem;
            }

            .controls {
                grid-template-columns: 1fr;
            }

            .image-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>AI Image Generator</h1>
            <p>Create stunning images from text descriptions using advanced AI technology</p>
        </div>

        <div class="generator-section">
            <div class="input-group">
                <label for="prompt">Enter your image description</label>
                <textarea 
                    id="prompt" 
                    class="prompt-input" 
                    placeholder="Describe the image you want to generate... (e.g., 'A futuristic cityscape at sunset with flying cars and neon lights')"
                ></textarea>
            </div>

            <div class="controls">
                <div class="control-group">
                    <label for="style">Art Style</label>
                    <select id="style" class="control-input">
                        <option value="realistic">Realistic</option>
                        <option value="artistic">Artistic</option>
                        <option value="cartoon">Cartoon</option>
                        <option value="abstract">Abstract</option>
                        <option value="cyberpunk">Cyberpunk</option>
                        <option value="vintage">Vintage</option>
                    </select>
                </div>

                <div class="control-group">
                    <label for="resolution">Resolution</label>
                    <select id="resolution" class="control-input">
                        <option value="512x512">512 × 512</option>
                        <option value="768x768">768 × 768</option>
                        <option value="1024x1024">1024 × 1024</option>
                        <option value="1536x1024">1536 × 1024</option>
                    </select>
                </div>

                <div class="control-group">
                    <label for="quality">Quality</label>
                    <select id="quality" class="control-input">
                        <option value="standard">Standard</option>
                        <option value="high">High</option>
                        <option value="ultra">Ultra</option>
                    </select>
                </div>

                <div class="control-group">
                    <label for="count">Number of Images</label>
                    <select id="count" class="control-input">
                        <option value="1">1 Image</option>
                        <option value="2">2 Images</option>
                        <option value="4">4 Images</option>
                    </select>
                </div>
            </div>

            <button id="generateBtn" class="generate-btn">
                <span class="loading-spinner"></span>
                <span class="btn-text">Generate Images</span>
            </button>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Generated Images</h2>
            </div>

            <div id="results">
                <div class="placeholder">
                    <svg class="placeholder-icon" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
                    </svg>
                    <p>Your generated images will appear here</p>
                    <p style="font-size: 0.8rem; margin-top: 0.5rem;">Enter a prompt above and click "Generate Images" to get started</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const promptInput = document.getElementById('prompt');
        const styleSelect = document.getElementById('style');
        const resolutionSelect = document.getElementById('resolution');
        const qualitySelect = document.getElementById('quality');
        const countSelect = document.getElementById('count');
        const generateBtn = document.getElementById('generateBtn');
        const resultsDiv = document.getElementById('results');
        const loadingSpinner = document.querySelector('.loading-spinner');
        const btnText = document.querySelector('.btn-text');

        let isGenerating = false;

        generateBtn.addEventListener('click', generateImages);

        promptInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && e.ctrlKey) {
                generateImages();
            }
        });

        function generateImages() {
            const prompt = promptInput.value.trim();
            
            if (!prompt) {
                showStatusMessage('error', 'Please enter a description for your image.');
                return;
            }

            if (isGenerating) return;

            isGenerating = true;
            generateBtn.disabled = true;
            loadingSpinner.style.display = 'inline-block';
            btnText.textContent = 'Generating...';

            // Clear previous results
            resultsDiv.innerHTML = '';

            // Show generating message
            showStatusMessage('info', 'Generating your images... This may take a few moments.');

            // Generate actual images
            setTimeout(() => {
                const imageCount = parseInt(countSelect.value);
                const resolution = resolutionSelect.value;
                const style = styleSelect.value;
                const quality = qualitySelect.value;

                generateImageCards(prompt, imageCount, resolution, style, quality);

                isGenerating = false;
                generateBtn.disabled = false;
                loadingSpinner.style.display = 'none';
                btnText.textContent = 'Generate Images';

                showStatusMessage('success', `Successfully generated ${imageCount} image${imageCount > 1 ? 's' : ''}!`);
            }, 2000); // Reduced timeout since we're making real API calls
        }

        async function generateImageCards(prompt, count, resolution, style, quality) {
            const imageGrid = document.createElement('div');
            imageGrid.className = 'image-grid';

            for (let i = 0; i < count; i++) {
                const imageCard = document.createElement('div');
                imageCard.className = 'image-card';

                // Create enhanced prompt with style
                const enhancedPrompt = `${prompt}, ${style} style, high quality, detailed`;
                
                // Generate actual image using Pollinations AI (free API)
                const imageUrl = `https://image.pollinations.ai/prompt/${encodeURIComponent(enhancedPrompt)}?width=${resolution.split('x')[0]}&height=${resolution.split('x')[1]}&seed=${Date.now() + i}&nologo=true`;

                imageCard.innerHTML = `
                    <div class="image-container" style="position: relative; overflow: hidden;">
                        <img src="${imageUrl}" 
                             alt="Generated image: ${prompt}" 
                             style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px 8px 0 0; transition: transform 0.3s ease;"
                             onload="this.style.opacity='1'"
                             onerror="this.parentElement.innerHTML='<div class=\\'image-placeholder\\'>Failed to generate image</div>'"
                             loading="lazy">
                        <div class="image-overlay" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); opacity: 0; transition: opacity 0.3s ease; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.9rem;">
                            Click to view full size
                        </div>
                    </div>
                    <div class="image-info">
                        <div class="image-prompt">"${prompt}"</div>
                        <div class="image-details">
                            <span>${resolution}</span>
                            <span>${style} style</span>
                            <span>${quality} quality</span>
                        </div>
                        <div style="margin-top: 0.5rem; display: flex; gap: 0.5rem;">
                            <button onclick="downloadImage('${imageUrl}', '${prompt.substring(0, 30)}')" 
                                    style="flex: 1; padding: 0.5rem; background: #4a9eff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">
                                Download
                            </button>
                            <button onclick="openImageModal('${imageUrl}', '${prompt}')" 
                                    style="flex: 1; padding: 0.5rem; background: #333; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">
                                View Full
                            </button>
                        </div>
                    </div>
                `;

                // Add hover effect
                imageCard.addEventListener('mouseenter', () => {
                    const overlay = imageCard.querySelector('.image-overlay');
                    if (overlay) overlay.style.opacity = '1';
                });

                imageCard.addEventListener('mouseleave', () => {
                    const overlay = imageCard.querySelector('.image-overlay');
                    if (overlay) overlay.style.opacity = '0';
                });

                imageGrid.appendChild(imageCard);
            }

            resultsDiv.appendChild(imageGrid);
        }

        function showStatusMessage(type, message) {
            const existingMessage = document.querySelector('.status-message');
            if (existingMessage) {
                existingMessage.remove();
            }

            const statusDiv = document.createElement('div');
            statusDiv.className = `status-message status-${type}`;
            statusDiv.textContent = message;

            resultsDiv.insertBefore(statusDiv, resultsDiv.firstChild);

            // Auto-remove success/info messages after 5 seconds
            if (type === 'success' || type === 'info') {
                setTimeout(() => {
                    if (statusDiv.parentNode) {
                        statusDiv.remove();
                    }
                }, 5000);
            }
        }

        // Add some sample prompts for demonstration
        const samplePrompts = [
            "A majestic mountain landscape at golden hour with a crystal clear lake reflecting the peaks",
            "A futuristic robot sitting in a cozy library reading a book",
            "An ancient Japanese temple surrounded by cherry blossoms in full bloom",
            "A steampunk airship floating above a Victorian city at sunset",
            "A magical forest with glowing mushrooms and ethereal light filtering through the trees"
        ];

        // Add click event to placeholder for sample prompt
        document.addEventListener('click', (e) => {
            if (e.target.closest('.placeholder') && !promptInput.value.trim()) {
                const randomPrompt = samplePrompts[Math.floor(Math.random() * samplePrompts.length)];
                promptInput.value = randomPrompt;
                promptInput.focus();
            }
        });

        // Download image function
        function downloadImage(imageUrl, filename) {
            const link = document.createElement('a');
            link.href = imageUrl;
            link.download = `ai-generated-${filename.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.jpg`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

        // Modal for full-size image viewing
        function openImageModal(imageUrl, prompt) {
            const modal = document.createElement('div');
            modal.style.cssText = `
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.9); display: flex; align-items: center;
                justify-content: center; z-index: 1000; cursor: pointer;
            `;

            modal.innerHTML = `
                <div style="max-width: 90%; max-height: 90%; position: relative;">
                    <img src="${imageUrl}" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 8px;">
                    <div style="position: absolute; top: -40px; left: 0; right: 0; text-align: center; color: white; font-size: 0.9rem;">
                        "${prompt}"
                    </div>
                    <button onclick="this.parentElement.parentElement.remove()" 
                            style="position: absolute; top: -40px; right: 0; background: #ff4444; color: white; border: none; 
                                   border-radius: 50%; width: 30px; height: 30px; cursor: pointer; font-size: 1.2rem;">×</button>
                </div>
            `;

            modal.onclick = (e) => {
                if (e.target === modal) modal.remove();
            };

            document.body.appendChild(modal);
        }
    </script>
</body>
</html>yBEsnLrr6UV-X-xAkNweefC9vrBoU5728w")

# Get input from the user
contents = input("Please enter a description for the image you want to generate: ")

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    # Display the image after saving
    from IPython.display import Image, display

    display(Image(filename='gemini-native-image.png'))
