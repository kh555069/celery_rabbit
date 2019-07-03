# Under construction


# celery_rabbit
RabbitMQ + Celery 分散式爬蟲

1. 安裝 RabbitMQ https://www.rabbitmq.com/download.html
`sudo apt-get update`
`sudo apt-get install erlang`
`sudo apt-get install rabbitmq-server`

2. `pip install -r pkg.txt`


## 設定 rabbit
`rabbitmqctl add_user USER_NAME PASSWD`

`rabbitmqctl set_user_tags USER_NAME administrator`

`rabbitmqctl set_permissions -p / USER_NAME ".*" ".*" ".*"`


## start
`rabbitmq-server`

`python start.py`

`celery -A worker worker --loglevel=info`

![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit1.png)
![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit2.png)
