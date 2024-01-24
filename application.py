# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import cv2

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static'

# # Load your trained model
# model = load_model('model2.h5')  # Replace with the path to your model file

# # Define the target size for resizing the images
# target_size = (224, 224)

# # Define a function for image preprocessing
# def preprocess_image(image_path, target_size=target_size):
#     # Open the image
#     img = Image.open(image_path)

#     # Resize or crop the image to the target size
#     img = img.resize(target_size)

#     # Convert the image to a NumPy array
#     img_array = np.array(img)

#     # Normalize pixel values to be between 0 and 1
#     img_array = img_array / 255.0

#     return img_array

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'image' not in request.files:
#         return redirect(request.url)

#     file = request.files['image']

#     if file.filename == '':
#         return redirect(request.url)

#     if file:
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         # Load and preprocess the uploaded image
#         img = cv2.imread(file_path)
#         img = cv2.resize(img,(150,150))
#         img = img/255.0  # Normalize pixel values
#         img_array = np.expand_dims(img, axis=0)

#         # Make a prediction using the loaded model
#         prediction = model.predict(img_array)[0][0]

#         # Render the result page with the prediction
#         return render_template('result.html', prediction=f"{prediction:.2f}" , file_path = file_path)

# if __name__ == '__main__':
#     app.run(port = 8000 , debug=True)


from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
from PIL import Image
import numpy as np
from tqdm import tqdm  # Optional: for progress bar
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Load your trained model
model = load_model('model2.h5')  # Replace with the path to your model file

# Define the target size for resizing the images
target_size = (224, 224)

# Define a function for image preprocessing
def preprocess_image(image_path, target_size=target_size):
    # Open the image
    img = Image.open(image_path)

    # Resize or crop the image to the target size
    img = img.resize(target_size)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Normalize pixel values to be between 0 and 1
    img_array = img_array / 255.0

    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        image_data = []
        max_shape = (224, 224, 4)  # Initialize with a dummy shape

        image_path = file_path

        # Preprocess the image
        processed_image = preprocess_image(image_path)

        # Append the image data and label to the list
        image_data.append((processed_image))

        # Ensure all images have the same shape by resizing them to max_shape
        X_resized = np.array([np.resize(item, max_shape) for item in image_data])
        print(len(X_resized))
        
        prediction = model.predict(X_resized)
        print(prediction)

        # Render the result page with the prediction
        return render_template('index.html', prediction=f"{prediction[0][0]:.2f}" , file_path = file_path)

if __name__ == '__main__':
    app.run(port = 8000 , debug=True)


