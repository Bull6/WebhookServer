import datetime
import os
 
a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'
 
today = datetime.datetime.today()
print( today.strftime("%d-%m-%Y") ) # '04/05/2017'
 
print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00


today = datetime.datetime.now()
date = today.strftime('%d-%m-%Y')
directory_folder = ("./logs/" + date)

    
if not os.path.exists(directory_folder): #Если пути не существует создаем его
    os.makedirs(directory_folder)
"""
with open(directory_folder, 'w') as file: # Открываем фаил и пишем
    file.write("этот текст создан автоматически")
"""