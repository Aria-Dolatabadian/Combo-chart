import matplotlib.pyplot as plt
import pandas as pd

# create a pandas DataFrame for the temperature and rainfall data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    '2020 Temperature': [21.2, 23.4, 25.6, 28.1, 31.4, 33.2, 34.5, 33.8, 31.5, 28.4, 25.1, 22.0],
    '2020 Rainfall': [4.1, 4.5, 6.3, 20.1, 93.2, 228.3, 349.8, 330.1, 237.6, 82.3, 17.2, 5.9]
})

# create a combo chart with temperature and rainfall data across two years
fig, ax1 = plt.subplots()

# plot the temperature data on the left y-axis
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.plot(data['Month'], data['2020 Temperature'], color='tab:blue', label='2020')
ax1.tick_params(axis='y')

# create a second y-axis on the right for the rainfall data
ax2 = ax1.twinx()

# plot the rainfall data on the right y-axis
ax2.set_ylabel('Rainfall (mm)')
ax2.bar(data['Month'], data['2020 Rainfall'], color='tab:green', alpha=0.5, label='2020')
ax2.tick_params(axis='y')

# add a legend to the chart
fig.legend(loc='upper right')

# set the chart title and show the chart
plt.title('Monthly Temperature and Rainfall Data (2020)')
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#create list of months
Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
         'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#create list for made up average temperatures
Avg_Temp = [35, 45, 55, 65, 75, 85, 95, 100, 85, 65, 45, 35]
#create list for made up average percipitation %
Avg_Percipitation_Perc = [.90, .75, .55, .10, .35, .05, .05, .08, .20, .45, .65, .80]
#assign lists to a value
data = {'Month': Month, 'Avg_Temp': Avg_Temp, 'Avg_Percipitation_Perc': Avg_Percipitation_Perc}
#convert dictionary to a dataframe
df = pd.DataFrame(data)
#Print out all rows
df[:12]
print(df)
#create bar plot for average temps by month
plt.title('Average Temperature by Month')
sns.barplot(x='Month', y='Avg_Temp', data=df, palette='summer')
# create line plot for average percipitation levels
plt.title('Average Percipitation Percentage by Month')
sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data=df, sort=False)
fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
ax1.set_title('Average Percipitation Percentage by Month', fontsize=16)
ax1.set_xlabel('Month', fontsize=16)
ax1.set_ylabel('Avg Temp', fontsize=16, color=color)
ax2 = sns.barplot(x='Month', y='Avg_Temp', data = df, palette='summer')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Avg Percipitation %', fontsize=16, color=color)
ax2 = sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data = df, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()
