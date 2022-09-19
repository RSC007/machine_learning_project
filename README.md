# machine_learning_project

Following things are required.
1. GIT-HUB
2. Docker, Docker-HUB
3. Heroku account

Create the virtual env
```
ubantu
virtualenv <env_name>
Activate: source venv/bin/activate
```
OR
```
Window
conda create -p <env_name> python==3.7 -y
Activate: conda activate <env_name>/ or <env_name>
```

Install Requirements.txt
```
pip install -r requirements.txt
```


To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = rushichitte1998@gmail.com
2. HEROKU_API_KEY = dcb786ad-bd01-4180-9989-6daaf0af75bf
3. HEROKU_APP_NAME = ml-regression-app-123


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

> Note: Image name for docker must be lowercase

To list docker images
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running containers in docker
```
docker ps
```

To stop docker containers
```
docker stop <container_id>
```