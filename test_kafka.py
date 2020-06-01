# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/28 14:09
@ file:     test_kafka.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 存入kafka信息
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
 #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
for i in range(3):
     msg = "msg %d" % i
     print(msg)
     producer.send('test', msg)
producer.close()

# 生产数据
from pykafka import KafkaClient
host = 'IP:9092, IP:9092, IP:9092'
client = KafkaClient(hosts = host)
# 生产者
topicdocu = client.topics['my-topic']
producer = topicdocu.get_producer()
for i in range(100):
    print(i)
    producer.produce('test message ' + str(i ** 2))
producer.stop()

# 读取本地所有topic信息
from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
for topic in client.topics:
    print(topic)

# 查看brokers信息
from pykafka import KafkaClient
client = KafkaClient(host="127.0.0.1:9092")
print(client.brokers)

for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    id = client.brokers[n].id
    print("host=%s | port=%s | broker.id=%s " %(host,port,id))

# 直接消费Kafka
from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['test']
# 获取 consumer 消费者
consumer = topic.get_simple_consumer(consumer_group="test",reset_offset_on_start=True)
for message in consumer:
    print(message)
    if message is not None:
        print(">>>>>>>>>>",message.offset)
        print(">>>>>>>>>>",message.value)

# 从zookeeper消费
from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['test']
balanced_consumer= topic.get_balanced_consumer(consumer_group='test',auto_commit_enable=True,reset_offset_on_start=True,zookeeper_connect='127.0.0.1:9092')

for message in balanced_consumer:
    if message is not None:
        print(message.offset, message.value)