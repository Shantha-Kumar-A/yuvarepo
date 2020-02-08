from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("data_histogram.csv")
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins = bins, edgecolor = "black", log = True)

median_age = 29
color = '#fc4f32' 
plt.axvline(median_age,color = color, label = 'Median Age', linewidth = 2)
plt.legend()

plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")
plt.tight_layout()

plt.show()