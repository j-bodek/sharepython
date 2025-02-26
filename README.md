# SharePython.io
Fully open source full stack platform, written in microservices architecture for sharing and executing python code from your browser (heavily inspired by [**codeshare.io**](https://codeshare.io/ "codeshare.io")). 

![sharepython_gif](images/sharepython.gif)

Stack:
- Django
- Django Rest Framework
- Sanic
- Vue
- MdBootstrap
- Redis
- Celery

Microservices:
- [Vue Frontend App](https://github.com/LilJack118/sharepython-frontend "Vue Frontend App")
- [Api (written mostly in drf)](https://github.com/LilJack118/sharepython-api "Api (written mostly in drf)")
- [Websocket Server](https://github.com/LilJack118/sharepython-websocket-server "Websocket Server")

### Run this project locally in few easy steps
Make sure you have docker installed before you start

#### 1.Clone this repository
```python
git clone https://github.com/LilJack118/sharepython.git
```

#### 2. Clone microservices repositories (if not already cloned)
```python
python3 clone.py
```

#### 4. Add env variables to api service (by adding .env file or uncomment environment lines in docker-compose file for api, celery_worker services)

#### 3. Run containers
```python
docker-compose build
docker-compose up
```
