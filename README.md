# Under construction


# celery_rabbit
RabbitMQ + Celery 分散式爬蟲

1. 安裝 RabbitMQ https://www.rabbitmq.com/download.html

2. `pip install -r pkg.txt`

## start
`rabbitmq-server`

`python start.py`

`celery -A worker worker --loglevel=info`

![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit1.png)
![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit2.png)
