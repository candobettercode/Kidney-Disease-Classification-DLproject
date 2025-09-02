import mlflow
import os


print("Current Tracking URI:", mlflow.get_tracking_uri())

print("MLFLOW_TRACKING_URI:", os.getenv("MLFLOW_TRACKING_URI"))
print("MLFLOW_TRACKING_USERNAME:", os.getenv("MLFLOW_TRACKING_USERNAME"))
print("MLFLOW_TRACKING_PASSWORD:", os.getenv("MLFLOW_TRACKING_PASSWORD"))

# Try starting a dummy run
with mlflow.start_run(run_name="test_connection"):
    mlflow.log_metric("test_metric", 1.0)

print("✅ Logged dummy run to MLflow/Dagshub")