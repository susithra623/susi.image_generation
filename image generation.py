from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key="AIzaSyBEsnLrr6UV-X-xAkNweefC9vrBoU5728w")

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