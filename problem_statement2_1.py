import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic_dataset = pd.read_csv(url)

male_data = titanic_dataset[titanic_dataset['sex'] == 'male']
female_data = titanic_dataset[titanic_dataset['sex'] == 'female']

male_data_proportion = len(male_data)/len(titanic_dataset)
female_data_proportion = len(female_data)/len(titanic_dataset)

sizes = [male_data_proportion, female_data_proportion]
labels = ['male count', 'female count']
explode = [0.1, 0]

#add colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.show()
