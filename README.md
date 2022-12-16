# SharePython.io
Fully open source full stack platform, written in microservices architecture for sharing and executing python code from your browser (heavily inspired by [**codeshare.io**](https://codeshare.io/ "codeshare.io")). 

Stack:
- Django
- Django Rest Framework
- Vue
- MdBootstrap

Microservices:
- [Vue Frontend App](https://github.com/LilJack118/sharepython-frontend "Vue Frontend App")
- [Api (written mostly in drf)](https://github.com/LilJack118/sharepython-api "Api (written mostly in drf)")
- Websocket Server
- Remote Code Execution Engine

### Run this project locally in few easy steps
Make sure you have docker installed before you start

#### 1.Clone this repository
```python
git clone https://github.com/LilJack118/sharepython.git
```

#### 2. Clone microservices repositories
```python
python3 clone.py
```

#### 3. Run containers
```python
docker-compose build
docker-compose up
```
