import pandas as pd
from fbprophet import Prophet

# Load historical CPU utilization data
data = pd.read_csv("gke_cpu_metrics.csv")
data.columns = ["ds", "y"]  # Prophet expects 'ds' (date) and 'y' (value)

# Train a predictive model
model = Prophet()
model.fit(data)

# Forecast for the next 7 days
future = model.make_future_dataframe(periods=7, freq="D")
forecast = model.predict(future)

# Save model
model.save("ai_autoscaler_model.pkl")
