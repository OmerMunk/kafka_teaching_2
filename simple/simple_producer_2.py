from random import randint

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')


# for i in range(10):
#     message = f'Bahur Ravak {i}'.encode('utf-8')
#     producer.send('gur_topic', message)
#     print(f'Sent {message}')


for i in range(1_000_000):
    target_id = randint(1, 10)
    target_x = randint(1, 100)
    target_y = randint(1, 100)
    target = (target_id, target_x, target_y)
    message = f'{target}'.encode('utf-8')
    producer.send('gur_topic', message)
producer.flush() # producer.flush is used to make sure that all messages are sent before closing the producer
producer.close() # close the producer
