import pandas as pd
import joblib
from django.conf import settings

class MLPredictionService:
    """
    Service class to handle ML model operations
    This encapsulates model loading and prediction logic
    """
    def __init__(self):
        self.model = None
        self.pipline = None
        self.load_model()
    
    def load_model(self):
        """
        load the ml model at startup
        This is called once when the service is instantiated
        """
        try:
            # load model from joblib file
            model_path = getattr(settings, 'MODEL_PATH', 'rf_model_pca_V01.joblib')
            self.model = joblib.load(model_path)
            pipeline_path = getattr(settings, 'PIPELINE_PATH', 'pipeline_pca_V01.joblib')
            self.pipline = joblib.load(pipeline_path)
        except Exception as e:
            raise Exception(f"Failed to load the model: {str(e)}")
        
    def preprocess_data(self, df):
        """
        apply preprocessing
        """
        return self.pipeline.transform(df)
    
    def predict(self, input_data):
        """
        Make prediction using the loaded model
        returns price
        """
        try:
            df = pd.DataFrame([input_data])
            processed = self.preprocess_data(df)
            prediction = self.model.predict(processed)
            price = float(prediction[0])
            return {
                'price':price
            }
        except Exception as e:
            raise Exception(f"Prediction failed: {str(e)}")
        
# create singleton instance_loaded once when django starts
ml_service = MLPredictionService()