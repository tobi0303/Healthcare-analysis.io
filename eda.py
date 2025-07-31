# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("er_admissions.csv", parse_dates=['timestamp'])

# Extract hour and date
df['hour'] = df['timestamp'].dt.hour
df['date'] = df['timestamp'].dt.date

# Plot hourly patient counts
hourly_counts = df.groupby('hour').size()
plt.figure(figsize=(10, 5))
sns.barplot(x=hourly_counts.index, y=hourly_counts.values, palette='viridis')
plt.title("Hourly ER Admissions")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Admissions")
plt.tight_layout()
plt.savefig("hourly_er_admissions.png")
plt.close()

# Wait time vs flu season
plt.figure(figsize=(10, 5))
sns.boxplot(x='is_flu_season', y='wait_time_min', data=df)
plt.title("Wait Time during Flu Season vs Non-Flu Season")
plt.xlabel("Flu Season")
plt.ylabel("Wait Time (min)")
plt.tight_layout()
plt.savefig("wait_time_flu_season.png")
plt.close()

# Wait time vs holidays
plt.figure(figsize=(10, 5))
sns.boxplot(x='is_holiday', y='wait_time_min', data=df)
plt.title("Wait Time on Holidays vs Non-Holidays")
plt.xlabel("Holiday")
plt.ylabel("Wait Time (min)")
plt.tight_layout()
plt.savefig("wait_time_holidays.png")
plt.close()