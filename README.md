# celery_rabbit
RabbitMQ + Celery 分散式爬蟲

簡單介紹一下，Celery 跟 RabbitMQ

*Celery*: 扮演著發送(Producer)以及處理(Worker)的角色，將工作發送到 Broker ，從 Broker ，取出工作來處理

*RabbitMQ*: MQ 是訊息佇列 Message Queue 的縮寫，負責接收與轉發訊息(工作)，而 Broker 就是負責處理 MQ 的地方。是用 erlang 開發的AMQP，常見的 Broker 有 RabbitMQ, Redis, Kafka

## Note
RabbitMQ 有時候會突然吃掉太多資源， 執行 `rabbitmqctl shutdown` 關掉 RabbitMQ。<br></br>
如果 `rabbitmqctl shutdown` 無效，執行 `kill -9 $(ps -ef | grep -e 'beam\.smp' | awk '{ print $2 }')` 強制關掉。

## Installation
1. 安裝 RabbitMQ https://www.rabbitmq.com/download.html<br></br>
`sudo apt-get update`<br></br>
`sudo apt-get install erlang`<br></br>
`sudo apt-get install rabbitmq-server`<br></br>

2. `pip install -r pkg.txt`


## Setting
`rabbitmqctl add_user USER_NAME PASSWD`

`rabbitmqctl set_user_tags USER_NAME administrator`

`rabbitmqctl set_permissions -p / USER_NAME ".*" ".*" ".*"`

設定完成後，從 `http://localhost:15672/` 登入即可進到管理介面
![image](https://github.com/kh555069/celery_rabbit/blob/master/port15672.png)

上圖是三台機器(電腦)連線， Broker 負責將工作分配到這三台機器上

## Start
`rabbitmq-server -detached`

`python start.py`

`celery -A worker worker --loglevel=info`

![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit1.png)
![image](https://github.com/kh555069/celery_rabbit/blob/master/celery_rabbit2.png)
