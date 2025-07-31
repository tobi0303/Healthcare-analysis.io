import warnings
warnings.filterwarnings("ignore", message="Importing plotly failed")

# forecast.py
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

model = Prophet

# Load data
df = pd.read_csv("er_admissions.csv", parse_dates=['timestamp'])

# Aggregate daily admissions
daily_df = df.groupby(df['timestamp'].dt.date).size().reset_index(name='y')
daily_df.rename(columns={'timestamp': 'ds'}, inplace=True)
daily_df['ds'] = pd.to_datetime(daily_df['ds'])

# Initialize and fit Prophet model
model = Prophet(daily_seasonality=True, yearly_seasonality=True)
model.fit(daily_df)

# Make future dataframe for next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot forecast
fig = model.plot(forecast)
plt.title("Forecasted Daily ER Admissions")
plt.xlabel("Date")
plt.ylabel("Admissions")
plt.tight_layout()
fig.savefig("forecast_er_admissions.png")
plt.close()