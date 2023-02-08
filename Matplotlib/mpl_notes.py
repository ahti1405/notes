# import numpy as np
# from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

# plt.xkcd() # comics style

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]

# # Median Python Developer Salaries by Age
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]

# # Median JavaScript Developer Salaries by Age
# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]



# Plot in the graph
# plt.plot(ages_x, dev_y, "k--", label="All Devs")
# plt.plot(ages_x, dev_y, color='k', linestyle="--", marker = '.', label="All Devs")
# We can use hex for colors
# plt.plot(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs")


# Python devs
# plt.plot(ages_x, py_dev_y, color='b', marker='o', label="Python")
# plt.plot(ages_x, py_dev_y, color="#5a7d9a", linewidth=3, label="Python")
# plt.plot(ages_x, py_dev_y, label="Python")


# JS devs
# plt.plot(ages_x, js_dev_y, color="#adad3b", linewidth=3, label="JS")
# plt.plot(ages_x, js_dev_y, label="JS")

# All devs... We put in the last because it is a dashet line and in will be plotted the last
# plt.plot(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs")

# Bar chart
# x_indexes = np.arange(len(ages_x))
# width = 0.25

# plt.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")
# plt.bar(x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")
# plt.bar(x_indexes + width, js_dev_y, width=width, color="#e5ae38", label="JavaScript")

# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
# plt.title("Median Salary (USD) by Age")

# # plt.legend(["All Devs", "Python"])
# plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.grid(True)

# plt.tight_layout()

# to save the graph as a file...will save as a png file in the current directory
# plt.savefig("plot.png")

# plt.show()

# working with csv file
# import csv
# from collections import Counter


# plt.style.use('fivethirtyeight')

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter)
# will print the most common 15
# print(language_counter.most_common(15))

# open and read file with pandas
# import pandas as pd

# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']

# language_counter = Counter()

# for response in lang_responses:
#     language_counter.update(response.split(';'))

# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# # If we want most popular language to appear at the top
# languages.reverse()
# popularity.reverse()

# plt.barh(languages, popularity)

# plt.title('Most Popular Languages')
# plt.xlabel('The Number of People Who Use')
# plt.ylabel('Programming Languages')

# plt.tight_layout()
# plt.show()

# Lesson 3 - Pie Charts
# from matplotlib import pyplot as plt


# plt.style.use('fivethirtyeight')

# # slices = [60, 40, 20, 20]
# # labels = ['Sixty', 'Forty', 'Twenty1', 'Twenty2']
# # # colors = ['red', 'green', 'blue', 'yellow']
# # colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']


# # Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# explode = [0, 0, 0, 0.1, 0]

# # plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
# plt.pie(slices, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={'edgecolor': 'black'})
# # autopct='%1.1f%%' - to show percentage on the slices

# plt.title('My Awesome Pie Chart')
# plt.tight_layout()

# plt.show()

# Lesson 4 - Stack Plots (Area Plots)

# from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')

# minutes = [1,2,3,4,5,6,7,8,9]

# player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
# player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
# player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# labels = ['player1', 'player2', 'player3']
# colors = ['#008fd5', '#fc4f30', '#6d904f']

# plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# # plt.legend(loc='upper left') # we can hardcode the location of legend
# plt.legend(loc=(0.07, 0.05)) # this means we want location of the legend to be 7% from the left and 5% from the bottom

# plt.title('My Awesome Stack Plot')
# plt.tight_layout()
# plt.show()

# Lesson 5 - Filling Area on Line Plots
# import pandas as pd
# from matplotlib import pyplot as plt

# data = pd.read_csv('data1.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

# plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

# plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287

# plt.fill_between(ages, py_salaries, alpha=0.25) # default y2=0, the thrid argument
# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries > overall_median), 
#                  interpolate=True, alpha=0.25)

# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries <= overall_median), 
#                  interpolate=True, color='red', alpha=0.25)

# plt.fill_between(ages, py_salaries, dev_salaries, 
#                  where=(py_salaries > dev_salaries), 
#                  interpolate=True, alpha=0.25, label='Above avg')

# plt.fill_between(ages, py_salaries, dev_salaries, 
#                  where=(py_salaries <= dev_salaries), 
#                  interpolate=True, color='red', alpha=0.25, label='Below avg')

# plt.legend()
# plt.title('Median Salary (USD) by Age')
# plt.ylabel('Median Salary (USD)')
# plt.xlabel('Ages')

# plt.tight_layout()
# plt.show()


# Lesson 6 - Histograms

# import pandas as pd
# from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')

# ages = [18,19,22,24,25,25,30,32,34,35,38,40,42,45,50,55]
# bins = [10,20,30,40,50,60]

# data = pd.read_csv('data_6.csv')
# ids = data['Responder_id']
# ages = data['Age']

# bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # plt.hist(ages, bins=5, edgecolor = 'black')
# plt.hist(ages, bins=bins, edgecolor = 'black', log=True)

# median_age = 29
# color = '#fc4f30'

# plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

# plt.legend(loc=(0.75, 0.9)) # 75% from the left and 90% from the bottom

# plt.title('Ages of Respondents')
# plt.xlabel('Ages')
# plt.ylabel('Total  Respondents')

# plt.tight_layout()
# plt.show()

# Lesson 7 - Scatter Plots
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')


# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# plt.scatter(x, y, s=100, c='green', marker='X') # s for size, c for color
# plt.scatter(x, y, s=100, c='green', edgecolor='black', linewidth=1, alpha=0.75)
# plt.scatter(x, y, s=100, c=colors, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.75)
# plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.75)

# cbar = plt.colorbar()
# cbar.set_label('Satisfaction')

data = pd.read_csv('data_7.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolors='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ration')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending Youtube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')



plt.tight_layout()
plt.show()