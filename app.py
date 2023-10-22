from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from resize_images import resize_image
import os

app = Flask(__name__)

# Define the allowed file extensions (modify this list as needed)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        square_fit_size = int(request.form['size'])
        new_folder_name = request.form['folder_name']

        # Create the output folder using os.path.join
        output_folder = os.path.join('static', new_folder_name)

        # Process the uploaded image files
        uploaded_files = request.files.getlist('images')

        resized_images = []
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):
                # Call the resize_image function and provide the output_folder
                result = resize_image(uploaded_file, output_folder, square_fit_size)
                if result:
                    resized_images.append(result)

        return render_template('results.html', resized_images=resized_images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
