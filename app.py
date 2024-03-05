#Author : Abhishek Bajpai (abhishek.bajpai.ca@gmail.com)
import os
from flask import Flask, request, render_template, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model("C:/CloudEngineeringPOCs/AI-ML-Edureka/AIML_POCs/CNN_ImageIDed/AI_ImageDetection_POC/trained_models/abeer_amiya_animals_classifier_model-v1.keras") #, custom_objects=custom_objects)  # Change to your model file path
#C:\CloudEngineeringPOCs\AI-ML-Edureka\AIML_POCs\CNN_ImageIDed\AI_ImageDetection_POC\trained_models\animals_model-v1.keras
#C:\CloudEngineeringPOCs\AI-ML-Edureka\AIML_POCs\CNN_ImageIDed\AI_ImageDetection_POC\trained_models\abeer_amiya_animals_classifier_model-v1.keras
# Function to preprocess and predict on the uploaded image
def load_and_predict(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    prediction = model.predict(img_array)
    return prediction

# Route for serving uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', message="No file uploaded")

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message="No file selected")

        if file:
            # Save the uploaded image
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)

            # Make predictions on the uploaded image
            prediction = load_and_predict(file_path)
            # class_indices = {0: 'Class 1', 1: 'Class 2', 2: 'Class 3'}  # Define your class labels
            # predicted_class = class_indices[np.argmax(prediction)]
            #class_labels = sorted(os.listdir("../data/training/people"))
            class_labels = sorted(os.listdir("C:/CloudEngineeringPOCs/AI-ML-Edureka/AIML_POCs/CNN_ImageIDed/data/training/animals"))  

            print(f'Class Labels Length : {len(class_labels)}')          
            predicted_class_index = np.argmax(prediction)
            print(f'Predicted Class Index : {type(predicted_class_index)} :  {predicted_class_index}')
            predicted_class = class_labels[predicted_class_index]

            return render_template('index.html', message="CNN Algorithm identified as : " + predicted_class, image_file='/uploads/' + filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
