from flask import Flask, request, render_template, send_file, after_this_request
from PIL import Image
import os

app = Flask(__name__)

def combine_images_vertically(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image1.width != image2.width:
        raise ValueError("The widths of the images must be the same.")

    combined_height = image1.height + image2.height
    combined_image = Image.new('RGB', (image1.width, combined_height))

    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, image1.height))

    combined_image.save(output_path)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image1' not in request.files or 'image2' not in request.files:
        return 'No file part'

    file1 = request.files['image1']
    file2 = request.files['image2']

    if file1.filename == '' or file2.filename == '':
        return 'No selected file'

    if file1 and file2:
        # Ensure the static directory exists
        if not os.path.exists('static'):
            os.makedirs('static')

        image1_path = os.path.join('static', file1.filename)
        image2_path = os.path.join('static', file2.filename)
        output_path = os.path.join('static', 'combined_image.png')

        file1.save(image1_path)
        file2.save(image2_path)

        try:
            combine_images_vertically(image1_path, image2_path, output_path)
        except ValueError as e:
            return str(e)

        @after_this_request
        def remove_file(response):
            try:
                os.remove(output_path)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)
            return response

        return send_file(output_path, mimetype='image/png', as_attachment=True, download_name='combined_image.png')

if __name__ == '__main__':
    app.run(debug=True)
