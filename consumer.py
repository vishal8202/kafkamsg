from kafka import  KafkaConsumer
bootstrap_server=["localhost:9092"]
topic="Test"
consumer=KafkaConsumer(topic,bootstrap_servers=bootstrap_server)
for i in consumer:
    print(str(i.value.decode()))