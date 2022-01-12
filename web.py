from flask import Flask, request
import json
import os
import datetime

app = Flask(__name__)


@app.route('/payload', methods=['POST'])
def logs():
    today = datetime.datetime.now()
    folder_path = "./logs/" + today.strftime("%d.%m.%Y") # Путь к папке с файлом
    
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
            print (i)
    downloadFromGit()
    return "OK"

def downloadFromGit():

    data = json.loads(request.data)

    folder_path = "./app/" + data['repository']['name'] # Путь к папке с файлом
    
    if not os.path.exists(folder_path): #Если пути не существует создаем его
        os.makedirs(folder_path)
        os.system('cd ' + folder_path + ' && git clone ' + data['repository']['ssh_url'] + ' .')
    else:
        os.system('cd ' + folder_path + ' && git pull origin ' + data['repository']['master_branch'] )



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4567)
