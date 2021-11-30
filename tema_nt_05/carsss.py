import uuid
from pprint import pprint
import csv
import json
import os
import pandas as pd

############ Creare csv, credeam ca trebuie sa facem documentul din linia de cod ##############
cars_to_list = [
    ['ID','Brand','Model','Year','HP','Price'],
    [uuid.uuid1(),'Opel','Astra',2002,101,1500],
    [uuid.uuid1(),'Mazda','6',2012,120,6000],
    [uuid.uuid1(),'Ford','Focus',2009,105,3700],
    [uuid.uuid1(),'Dacia','Sandero',2010,76,3200],
    [uuid.uuid1(),'Skoda','Superb',2014,170,16450],
    [uuid.uuid1(),'Mercedes-Benz','S-Klasse',2021,524,297500],
    [uuid.uuid1(),'Maserati','Levante',2020,430,87699],
    [uuid.uuid1(),'Rolls-Royce','Ghost Black',2017,612,232633],
    [uuid.uuid1(),'McLaren','570GT',2018,570,184800],
    [uuid.uuid1(),'Aston Martin','DBX',2021,551,214184],
    [uuid.uuid1(),'Ferrari','812',2018,799,324870],
    [uuid.uuid1(),'Porche','Taycan Turbo',2021,761,175049],
    [uuid.uuid1(),'BMW','iX',2021,326,101699]
]

with open('cars_list.csv','a',newline = '') as file:
    csv_writer = csv.writer(file, delimiter=',')
    for car in cars_to_list:
        csv_writer.writerow(car)

################ Ce am inteles ca trebuie sa fac prima data ###########
#
# cars = [
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Opel',
#         'Model': 'Astra',
#         'Year': 2002,
#         'HP': 101,
#         'Price': 1500
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Mazda',
#         'Model': '6',
#         'Year': 2012,
#         'HP': 120,
#         'Price': 6000
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Ford',
#         'Model': 'Focus',
#         'Year': 2009,
#         'HP': 105,
#         'Price': 3700
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Dacia',
#         'Model': 'Sandero',
#         'Year': 2010,
#         'HP': 76,
#         'Price': 3200
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Skoda',
#         'Model': 'Superb',
#         'Year': 2014,
#         'HP': 170,
#         'Price': 16450
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Mercedes-Benz',
#         'Model': 'S-Klasse',
#         'Year': 2021,
#         'HP': 524,
#         'Price': 297500
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Maserati',
#         'Model': 'Levante',
#         'Year': 2020,
#         'HP': 430,
#         'Price': 87699
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Rolls-Royce',
#         'Model': 'Ghost Black',
#         'Year': 2017,
#         'HP': 612,
#         'Price': 232633
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'McLaren',
#         'Model': '570GT',
#         'Year': 2018,
#         'HP': 570,
#         'Price': 184800
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Aston Martin',
#         'Model': 'DBX',
#         'Year': 2021,
#         'HP': 551,
#         'Price': 214184
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Ferrari',
#         'Model': '812',
#         'Year': 2018,
#         'HP': 799,
#         'Price': 324870
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'Porche',
#         'Model': 'Taycan Turbo',
#         'Year': 2021,
#         'HP': 761,
#         'Price': 175049
#     },
#     {
#         'ID': uuid.uuid1(),
#         'Brand': 'BMW',
#         'Model': 'iX',
#         'Year': 2021,
#         'HP': 326,
#         'Price': 101699
#     }
# ]

# slow_cars = [car for car in cars if car['HP'] < 120]
# pprint(sorted(slow_cars, key=lambda sc: sc.get('HP')))

# fast_cars = [car for car in cars if 120 <= car['HP'] < 180]
# pprint(sorted(fast_cars, key=lambda fc: fc.get('HP')))

# sport_cars = [car for car in cars if car['HP'] >= 180]
# pprint(sorted(sport_cars, key=lambda spc: spc.get('HP')))

# cheap_cars = [car for car in cars if car['Price'] < 10000]
# pprint(sorted(cheap_cars, key=lambda cc: cc.get('Price')))

# medium_cars = [car for car in cars if 10000 <= car['Price'] < 100000]
# pprint(sorted(medium_cars, key=lambda mc: mc.get('Price')))

# expensive_cars = [car for car in cars if car['Price'] > 100000]
# pprint(sorted(expensive_cars, key=lambda ec: ec.get('Price')))

##################### Ce cred ca e bine, doar cred :) ###########################################

main_dir ='C:/Users/O85108826/PycharmProjects/Mihai_scoala_informala/tema_nt_05/all_json'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

df = pd.read_csv(r'cars_list.csv')

df_slow_cars = df[(df.HP < 120)]
df_slow_cars.to_json(r'all_json/slow_cars.json', orient='records', lines= True)

df_fast_cars = df[(df.HP >= 120) & (df.HP < 180)]
df_fast_cars.to_json(r'all_json/fast_cars.json', orient='records', lines= True)

df_sport_cars = df[(df.HP >= 180)]
df_sport_cars.to_json(r'all_json/sport_cars.json', orient='records', lines= True)

df_cheap_cars = df[(df.Price < 10000)]
df_cheap_cars.to_json(r'all_json/cheap_cars.json', orient='records', lines= True)

df_medium_cars = df[(df.Price >= 10000) & (df.Price < 100000)]
df_medium_cars.to_json(r'all_json/medium_cars.json', orient='records', lines= True)

df_expensive_cars = df[(df.Price > 100000)]
df_expensive_cars.to_json(r'all_json/expensive_cars.json', orient='records', lines= True)

df_opel_cars = df[(df.Brand == 'Opel')]
df_opel_cars.to_json(r'all_json/opel_cars.json', orient='records', lines = True)

##### Sterge directorul cu fisierele aferente, la nevoie
# import pandas as pd
# import errno
# import stat
# import shutil

# def handleRemoveReadonly(func, path, exc):
#     excvalue = exc[1]
#     if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
#         os.chmod(main_dir, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO)
#         func(main_dir)
#     else:
#         raise
# shutil.rmtree('all_json', ignore_errors= False, onerror= handleRemoveReadonly )

##### Scrie cate un json pentru fiecare brand in parte, de fapt pentru fiecare rand.
##### Nu am reusit altfel, doar daca faceam mai ca mai sus, dar asta nu era o solutie daca aveam o lista cu 150 de branduri.
# csv_file = open('cars_list.csv','r')
# lines = csv_file.readlines()
#
# x=lines[0].split(",")
#
# for i in range(1, len(lines)):
#     y = lines[i].split(",")
#     data={x[0]:y[0],x[1]:y[1],x[2]:y[2],x[3]:y[3],x[4]:y[4],x[5].replace("\n",""):y[5].replace("\n","")}
#     js_file = open(str(i)+'.json','w+')
#     js_file.write(str(data))
#     js_file.close()
# csv_file.close()










