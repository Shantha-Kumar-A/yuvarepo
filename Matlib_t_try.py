import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
plt.style.use('fivethirtyeight')

# with open('data.csv') as csv_file:
# 	csv_reader = csv.DictReader(csv_file)
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_response = data['LanguagesWorkedWith']

language_counter = Counter()
	# for row in csv_reader:
	# 	language_counter.update(row['LanguagesWorkedWith'].split(';'))
for response in lang_response:
	language_counter.update(response.split(';'))

languages = []
popularity = []

for items in language_counter.most_common(15):
	languages.append(items[0])
	popularity.append(items[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)
# plt.ylabel('Programming Languages')
plt.xlabel('Number of users who use')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.savefig('programming_plot.png') #to save the plot to the cur dir
plt.show()