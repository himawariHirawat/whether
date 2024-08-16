import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# Make sure to provide the correct path to your CSV file
df = pd.read_csv('/home/hemant/important/tkinter/global_temperature.csv')

# Print the first few rows of the dataframe to verify its structure
print("DataFrame loaded:")
print(df.head())
# Check if the DataFrame is empty
if df.empty:
    print("DataFrame is empty. Please check the CSV file.")
    exit()

# Convert the 'dt' column to datetime format and extract the year
df['Year'] = pd.to_datetime(df['dt']).dt.year

# Optionally, you can set the 'Year' as the index if needed
# df.set_index('Year', inplace=True)

# Now you can continue with your analysis or plotting
# For example, plotting the average temperature over the years

# Group by year and calculate the average temperature
avg_temp_per_year = df.groupby('Year')['AverageTemperature'].mean().reset_index()

# Plotting the average temperature over the years
plt.figure(figsize=(12, 6))
plt.plot(avg_temp_per_year['Year'], avg_temp_per_year['AverageTemperature'], marker='o')
plt.title('Average Global Temperature Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Calculate Temperature Anomaly
# Assuming you have a column 'Base_Temperature' representing the baseline average temperature
df['Temperature_Anomaly'] = df['Global_Temperature'] - df['Base_Temperature']

# Plotting Temperature Anomaly
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['Temperature_Anomaly'], label='Temperature Anomaly', color='red', linewidth=2)
plt.title('Global Temperature Anomaly Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid()
plt.legend()
plt.show()

# Additional Analysis
# Resampling data to show 5-year averages
df_resampled = df.resample('5Y').mean()

# Plotting 5-Year Average Temperature
plt.figure(figsize=(14, 7))
plt.plot(df_resampled.index, df_resampled['Global_Temperature'], label='5-Year Average Global Temperature', color='orange', linewidth=2)
plt.title('5-Year Average Global Temperature Change')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.legend()
plt.show()
