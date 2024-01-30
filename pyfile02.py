# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:44:21 2024

@author: Janica van Wyk
"""

# 3. Storing Data in Python

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

# Storing Data
"""
B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 = 25
B11 = 39

print(B1)
print(B2)
print(B3)
print(B4)
print(B5)
print(B6)
print(B7)
print(B8)
print(B9)
print(B10)
print(B11)
"""
# Using Lists

age = [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
print(age)

"""
Lists indexes start at 0

print(age[0])
print(age[1])
print(age[10])

Error: No data at index 11:
print(age[11])
"""

# Basic Stats

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

print(age[0:3])     #if you want to print index 0, 1, and 2, use range 0:2+1

age.append(100)     #add 100 to end

# Storing Text
"""
C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)
"""
# Gender List

gender = ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"]
"""
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
"""

# Country List

country = ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]

print(country)
print(country[0])
print(country[5])

# 3.1 Lists

# Data Storage With Lists

my_list = [42, -2021, 6.283,"tau", "node"]

print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

print(my_list[0:3])
print("\b")

# 3.2 Dictionaries

"""
Dictionaries - key:value pairs

cat: "a cute animal"

- unordered
"""

d = {'key1': 'value1', 'key2': 'value2'}


mammals = {"cat": "a cute animal", "lion": "king of the jungle", "elephant": "a gigantic herbivore"}

print(mammals["cat"])

"""
person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'
"""

# 3.3 Data Frame

"""df = dataframe
pd = pandas
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
        'fruits': fruits,
        'sizes': size_nm
        }

import pandas as pd
    
df = pd.DataFrame(fruit_sizes)

print(df['fruits'])
print(df['sizes'])

print(df['sizes'].min())
print(df['sizes'].max())
print(df['sizes'].mean())
print(df.describe())

print(df[df['sizes'] > 10])

print(df[1:3])

# Add or remove column data

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns = ["sizes"], inplace=True)

