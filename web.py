from flask import Flask, request
import json
import os
from sys import argv
import datetime

app = Flask(__name__)

script, porT, app_dir = argv #Передаем переменные при запуске скрипта. Порт типа integer. Путь формата /dir1/dir2/../dirN


@app.route('/payload', methods=['POST'])
def downloadFromGit(): #Загрузка из GitHub

    data = json.loads(request.data)

    folder_path = app_dir + '/' + data['repository']['name'] # Путь к папке проекта
    
    if not os.path.exists(folder_path): #Если пути не существует создаем его и копируем проект из гита
        os.makedirs(folder_path)
        #os.system('exec ./git_clone.sh ' + folder_path + ' ' + data['repository']['ssh_url']) ОТКАЗЫВАЕТ В ДОСТУПЕ ........
        os.system('cd ' + folder_path + ' && git clone ' + data['repository']['ssh_url'] + ' .')
    else:
        #os.system('exec ./git_pull.sh ' + folder_path + ' ' + data['repository']['master_branch'])
        os.system('cd ' + folder_path + ' && git pull origin ' + data['repository']['master_branch'] )
    
    
    logs()
    
    return "OK"

def logs(): #Пишем логи
    
    today = datetime.datetime.now()
    folder_path = "./logs/" + today.strftime("%d.%m.%Y") # Путь к папке 
    
    if not os.path.exists(folder_path): #Если пути не существует создаем его
        os.makedirs(folder_path)
    
    data = json.loads(request.data)

    log_text = ("Repo_Name: {}".format(data['repository']['name']),
          "Pivate: {}".format(data['repository']['private']),
          "New commit by: {}".format(data['commits'][0]['author']['name']),
          "SSH_URL: {}".format(data['repository']['ssh_url']),
          "Branch: {}".format(data['repository']['master_branch']),
          "Head_Commit: {}".format(data['head_commit']['message']),
          "added: {}".format(data['head_commit']['added']),
          "removed: {}".format(data['head_commit']['removed']),
          "modified: {}".format(data['head_commit']['modified']))
    
    file_name = "/Commit by {} at ".format(data['commits'][0]['author']['name'])+today.strftime("%H-%M-%S") 
    with open(folder_path + file_name + '.txt', 'w') as file: # Открываем фаил и пишем
        for i in log_text:
            file.write(i + '\n')
            





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=porT)
