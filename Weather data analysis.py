import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

print("\t\t\tWELCOME TO DATA ANALYTICS\n")
time.sleep(2)
print("Let's start with the analysis of a 'WEATHER REPORT' recorded throught out the year at the hilly areas\n")
time.sleep(3)
print("Reading the report.....\n")
time.sleep(2)
data=pd.read_csv('Weather Data.csv')


print("Table:")
print(data)
time.sleep(3)

print("\n\n           \t\t\t\tDATA EXPLORATION            \t")
print("Exploring data.......")
time.sleep(2)


print("\n1.Table Info:\n")
time.sleep(2)
print(data.info())
time.sleep(3)

print("\n\n2.Table Description:\n")
time.sleep(2)
print(data.describe())
time.sleep(3)

print("\n\n3.Shape:\n")
time.sleep(2)
print(data.shape)

time.sleep(1)
print("\nSo we have 8784 rows and 8 columns")

time.sleep(3)
print("\n\n4.Indices:\n")
time.sleep(2)
print(data.index)

time.sleep(2)

print("\n\n5.Columns:\n")
time.sleep(2)
print(data.columns)

time.sleep(3)


print("\n\n6.Dtypes:\n")
time.sleep(2)
print(data.dtypes)
time.sleep(3)

print("\n\n7.Table elements:\n")
time.sleep(2)
print("\t7.1 Unique values of Temperature(in C) observed:\n")
time.sleep(2)
print("\t",data['Temp_C'].unique())
time.sleep(2)


print("\n\t7.2 Unique values of Dew points(in C) observed:\n")
time.sleep(2)
print("\t",data['Dew Point'].unique())
time.sleep(2)


print("\n\t7.3 Unique values of Relative humidity observed:\n")
time.sleep(2)
print("\t",data['Rel Hum_%'].unique())
time.sleep(2)

print("\n\t7.4 Unique values of Wind Speed(in kmph) observed:\n")
time.sleep(2)
print("\t",data['Wind Speed'].unique())
time.sleep(2)


print("\n\t7.5 Unique values of Visibility(in km) observed:\n")
time.sleep(2)
print("\t",data['Visibility_km'].unique())
time.sleep(2)



print("\n\t7.6 Unique values of Pressure(in kPa) observed:\n")
time.sleep(2)
print("\t",data['Press_kPa'].unique())
time.sleep(2)

print("\n\t7.7 Unique types of Weather observed:\n")
time.sleep(2)
lst=list(data['Weather'])
string = ",".join(lst)
output = string.split(",")
print("\t",list(set(output)))
time.sleep(2)


print("\n\n8. Total number of Elements:\n")
time.sleep(2)
print(data.count())
time.sleep(2)

print("\n\n9. Total number of Unique  elements:\n")
time.sleep(2)
print(data.nunique())
time.sleep(2)

print("\n\n           \t\t\t\tDATA ANALYSIS            \t")
time.sleep(2)
print("\n\nQuestion 1. Which is the most common weather?\n")
time.sleep(2)
dic={}
lst1=list(data['Weather'])
for m in lst1:
    if m not in dic.keys():
        dic[m]=lst1.count(m)
keymax=max(dic,key=dic.get)
print(keymax)
time.sleep(1)
print("\nHence,"+str(keymax)+" is the most common weather throughout the year.")
time.sleep(3)
print("\n\nQuestion 2.What is the average temperature ?\n")

time.sleep(2)

d1=data['Temp_C'].mean()
print(round(d1),"C")
time.sleep(1)
print("\nHence,"+str(round(d1))+"C is the average temperature throughout the year.")

time.sleep(3)
print("\n\nQuestion 3. Which is the highest wind speed observed?\n")

time.sleep(2)

d2=data['Wind Speed'].max()
print(d2,"km/h")
time.sleep(1)
print("\nHence,"+str(d2)+"km/h is the highest Wind speed seen throughout the year.")

time.sleep(3)

print("\n\nQuestion 4. Which is the lowest dew point observed ?\n")
time.sleep(2)
d3=data['Dew Point'].min()
print(d3,"C")
time.sleep(1)
print("\nHence,"+str(d3)+"C is the lowest dew point observed throughout the year.")
time.sleep(3)

print("\n\nQuestion 5. What is the average relative humidity seen ?\n")
time.sleep(2)
d4=data['Rel Hum_%'].mean()
print(round(d4))
time.sleep(1)
print("\nHence,"+str(round(d4))+" is the average Relative humidity seen throughout the year.")
time.sleep(2)
print("\n\nQuestion 6. What is the average wind speed observed throughout the year ?\n")
time.sleep(2)
d5=data['Wind Speed'].mean()
print(round(d5),"km/h")
time.sleep(1)
print("\nHence,"+str(round(d5))+"km/h is average wind speed in a year.")
time.sleep(2)
print("\n\nQuestion 7. What is the highest visibility distance seen in a year ?\n")
time.sleep(2)
d6=data['Visibility_km'].max()
print(d6,"km")
time.sleep(1)
print("\nHence,"+str(d6)+"km is the highest visibility distance.")
time.sleep(2)
print("\n\nQuestion 8. What is the variance of temperature throughout the year ?\n")
time.sleep(2)
d7=data['Temp_C'].var()
print(round(d7,2))
time.sleep(1)
print("\nThus,"+str(round(d7,2))+" is the variance of temperature in a year.")
time.sleep(2)
print("\n\nQuestion 9. What is the standard deviation of dew points in the year ?\n")
time.sleep(2)
d8=data['Dew Point'].std()
print(round(d8,2))
time.sleep(1)
print("\nTherefore,"+str(round(d8,2))+" is the standard deviation of dew points observed")
time.sleep(2)
print("\n\nQuestion 10. What is\ are the most rare weather observed throughout the year ?\n")
time.sleep(2)
dic={}
lst1=list(data['Weather'])
for m in lst1:
    if m not in dic.keys():
        dic[m]=lst1.count(m)
keymax=min(dic,key=dic.get)
print(keymax)
time.sleep(1)
print("\nHence, "+str(keymax)+" are the most rare weather observed in a year.")
time.sleep(2)

print("\n\n           \t\t\t\tDATA VISUALIAZTION            \t")
time.sleep(2)
print("\nSTEP 1: Optimising data for plotting....")
import numpy as np
data1=np.array_split(data,366)
lst=[]
for i in data1:
    arr=np.array(list(i.mean()))
    lst.append(arr)
output=pd.DataFrame(lst,columns=['Temp_C','Dew Point','Rel Hum_%','Wind Speed','Visibility_km','Press_km'])
time.sleep(1)
print("\nSTEP 2: Preparing Matplotlib...")
time.sleep(2)
print("\nSTEP 3: Making graphs...")
time.sleep(2)
print("\nSTEP 4: Plotting....")
time.sleep(1)
print("\n\nTHANKS,\nMADE BY ANANT GUPTA.")
output.hist(grid=False,figsize=(7,7))
time.sleep(2)
sns.pairplot(output)
time.sleep(2)


plt.figure(figsize=(15,10))
plt.plot(list(output['Temp_C']), "r-",label="Temperature")
plt.plot(list(output['Dew Point']), "g-",label="Dew Points")
plt.plot(list(output['Rel Hum_%']), "y-",label="Relative Humidity")
plt.plot(list(output['Wind Speed']), "b-",label="Wind Speed")
plt.plot(list(output['Visibility_km']),linestyle="-",color="black",label="Visibility")
plt.legend()
plt.title("Visualisation of Data")
plt.xticks(rotation=90)
plt.show()
