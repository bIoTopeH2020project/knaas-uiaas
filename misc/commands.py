import subprocess

def stop (x):
    bashCommand = "sudo docker container stop $(sudo docker ps -a -q  --filter ancestor=" + x + ")"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return;

def exe (x):
    bashCommand = "sudo docker exec -it $(sudo docker ps -a -q  --filter ancestor=" + x + ") /bin/sh"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return;

def host ():
    bashCommand = "sudo docker inspect $(sudo docker ps -a -q  --filter ancestor=mongo) | grep -i address"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return;

def run ():
    bashCommand = 'cd ..;sudo docker swarm init;sudo docker stack deploy -c docker-compose.yml firstcompose'
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return;

def modi(x):
    if x == 'firstimage':       
        bashCommand = 'cd ..;cd pysite;cd web;sudo docker build -t ' + x + ' .; sudo docker run -p 4000:80 ' + x
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return;
    
    elif x == 'nodeimage':        
        bashCommand = 'cd ..;cd pysite;cd Nodejs;sudo docker build -t ' + x + ' .; sudo docker run -p 5080:5080 -p 8090:8090 ' + x
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return;
    
    elif x == 'mongo':        
        bashCommand = 'cd ..;cd mongodb;sudo docker build -t ' + x + ' .; sudo docker run -p 27017:27017 ' + x
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return;
    
    elif x == 'node-red':
        bashCommand = 'cd ..;cd node-red;sudo docker build -t ' + x + ' .; sudo docker run -p 1880:1880 ' + x
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return;
    
    elif x == 'o-mi-node':
        bashCommand = 'cd ..;cd o-mi-node;sudo docker build -t ' + x + ' .; sudo docker run -p 8080:8080 ' + x
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return;
    
    return;
    
def stopall ():
    bashCommand = 'cd ..;sudo docker swarm leave --force'
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return;



