# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
trip_by_distance = pd.read_csv(r"Trips_by_Distance.csv", encoding='latin-1')
trip_full_data = pd.read_csv(r"Trips_Full_Data.csv", delimiter='\t')  # Set the delimiter to '\t' for tab-separated data


# Calculate the average number of people staying at home per week
avg_people_staying_at_home = trip_by_distance.groupby('Week')['Population Staying at Home'].mean()



# Visualization - Average number of people staying at home per week
plt.figure(figsize=(10, 6))
avg_people_staying_at_home.plot(kind='bar', color='skyblue')
plt.title('Average Number of People Staying at Home per Week')
plt.xlabel('Week of Date')
plt.ylabel('Average Population Staying at Home')
plt.show()

