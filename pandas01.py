# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:42:44 2024

@author: Janica van Wyk
"""

# 3. Reading in Files With Pandas


# Country

import pandas

print("Country Data\n")

file1 = pandas.read_csv("country_data.csv")

print(file1)
print("\n")

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

print(file1.info())
print("\n")

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 - whole number
 1   Gender   11 non-null     object - string
 2   Country  11 non-null     object - string
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
"""

print(file1.describe())
print("\n")

"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""

# Iris

print("Iris\n")

file2 = pandas.read_csv("iris.csv")

print(file2)
print("\n")

print(file2.info())
print("\n")

print(file2.describe())
print("\n")

# Diab data

print("Diab Data\n")

file3 = pandas.read_csv("diab_data.csv")

print(file3)
print("\n")

print(file3.info())
print("\n")

print(file3.describe())
print("\n")

# Housing data
# No column names

print("Housing Data\n")

column_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

file4 = pandas.read_csv("housing_data.csv", names = column_names)

print(file4)
print("\n")

print(file4.info())
print("\n")

print(file4.describe())
print("\n")

# Insurance data

print("Insurance Data\n")

file5 = pandas.read_csv("insurance_data.csv")

print(file5)
print("\n")

print(file5.info())
print("\n")

print(file5.describe())
print("\n")

# Original Insurance Data: Skip rows

file6 = pandas.read_csv("insurance_data - Copy.csv",skiprows=5)

print(file6)
print("\n")

print(file6.info())
print("\n")

print(file6.describe())
print("\n")

# Text files, ; instead ; of ,. Ex:
#file6 = pandas.read_csv("insurance_data - Copy.txt",sep=";")