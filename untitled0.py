import numpy as np

#Create an array of 10 zeros 
zero=np.zeros(10)
print(zero)

#Create an array of 10 ones
one=np.ones(10)
print(one)

#Create an array of 10 fives
five=np.ones(10)
print(five*5)

#Create an array of the integers from 10 to 50
integers=np.arange(10,51)
print(integers)

#Create an array of all the even integers from 10 to 50
even=[num for num in range(10,51) if num %2==0]
print(even)

#Create a 3x3 matrix with values ranging from 0 to 8
my_matrix = np.arange(9).reshape((3, 3))
print(my_matrix)

#Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

#Use NumPy to generate a random number between 0 and 1
rand0=np.random.rand()
print(rand0)

#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
rand2=np.random.rand(25)
print(rand2)

#Create the following matrix:
matrix = np.arange(0.01,1.01,0.01).reshape(10,10)
print(matrix)

#Create an array of 20 linearly spaced points between 0 and 1:
line=np.linspace(0,1,20)
print(line)





import pandas as pd
 #Read in the african_econ_crises.csv file that is located under the 01-Crash-Course-Pandas folder. Pay close attention to where the .csv file is located! Please don't post to the QA forums if you can't figure this one out, instead, run our solutions notebook directly to see how its done.**
data = pd.read_csv(r'african_econ_crises.csv')
print(data)

# Display the first 5 rows of the DataFrame
data = pd.read_csv(r'african_econ_crises.csv')
print(data.head())

# Count the number of unique countries in the 'country' column
data = pd.read_csv(r'african_econ_crises.csv')
num_countries = data['country'].nunique()
print("Number of countries represented in the dataset:", num_countries)
