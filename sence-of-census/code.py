# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data,new_record))
print(census)

print(np.shape(data))
print(np.shape(census))

age=census[:,0]
print(age)
max_age=np.max(age)
print(max_age)

min_age=np.min(age)
print(min_age)

age_mean=np.mean(age)
print(round(age_mean,2))

age_std=np.std(age)
print(round(age_std,2))

race_0=np.array([])
race_1=np.array([])
race_2=np.array([])
race_3=np.array([])
race_4=np.array([])


for i in census[:,2]:
    if i ==0:
        race_0=np.insert(race_0,0,i)

    elif i == 1:
        race_1=np.insert(race_1,0,1)

    elif i == 2:
        race_2=np.insert(race_2,0,i)

    elif i==3:
        race_3=np.insert(race_3,0,i)
    elif i==4:
        race_4=np.insert(race_4,0,i)
print(race_0)

len_0=len(list(race_0))
len_1=len(list(race_1))
len_2=len(list(race_2))
len_3=len(list(race_3))
len_4=len(list(race_4))

min = min(len_0,len_1,len_2,len_3,len_4)
print(min)

if len_0==min:
    minority_race=0
elif len_1 == min:
    minority_race=1

elif len_2==min:
    minority_race=2
elif len_3==min:
    minority_race=3
elif len_4 == min:
    minority_race=4

print(minority_race)


senior_citizens=census[census[:,0]>60]
senior_citizens

working_hours_sum=senior_citizens.sum(axis=0)[6]
working_hours_sum

senior_citizens_len=len(list(senior_citizens))

avg_working_hours = working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=high.sum(axis=0)[7]/len(list(high))
print(round(avg_pay_high,2))

avg_pay_low=low.sum(axis=0)[7]/len(list(low))
print(round(avg_pay_low,2))





