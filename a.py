from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Endpoint for image processing
@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the uploaded image
        image_file = request.files['image']

        if image_file:
            # Read the image
            image = Image.open(image_file)
            
            # Process the image using Tesseract OCR
            text = pytesseract.image_to_string(image)

            # Return the OCR result
            return jsonify({'result': text})
        else:
            return jsonify({'error': 'No image provided'})

    except Exception as e:
        return jsonify({'error': str(e),'name':'hello'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
