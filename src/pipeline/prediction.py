import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from src import logging

class PredictionPipeline:

    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        logging.info(f"predict function invoked..")

        # load model
        model = load_model(os.path.join("model","model.h5"))
        logging.info(f"Model Loaded..")
        
        # preprocess image
        test_image = image.load_img(self.filename, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # model prediction
        preds = model.predict(test_image)
        result = np.argmax(preds, axis=1)[0]
        confidence = float(np.max(preds))  

        logging.info(f"Prediction calculated...")


        # round confidence to 2 decimal places
        confidence = round(confidence, 2)

        if result == 1:
            label = "Tumor"
        else:
            label = "Normal"

        logging.info(f"RESULT>> label: {label}, confidence: {confidence}")
        return { "label": label, "confidence": confidence }
            
        '''
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Tumor"
            return [{ "image" : prediction}]   
        else:
            prediction = "Normal"
            return [{ "image" : prediction}]      
        '''

