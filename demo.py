import mlflow
import os
import gdown


print("Current Tracking URI:", mlflow.get_tracking_uri())

print("MLFLOW_TRACKING_URI:", os.getenv("MLFLOW_TRACKING_URI"))
print("MLFLOW_TRACKING_USERNAME:", os.getenv("MLFLOW_TRACKING_USERNAME"))
print("MLFLOW_TRACKING_PASSWORD:", os.getenv("MLFLOW_TRACKING_PASSWORD"))

''' 
# Try starting a dummy run
with mlflow.start_run(run_name="test_connection"):
    mlflow.log_metric("test_metric", 1.0)

print("✅ Logged dummy run to MLflow/Dagshub")
'''

file_id = "1dXJvoFA95jfTKY_2sbvr4pdGDCwjpfRl"
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, "data.zip", quiet=False, verify=False)