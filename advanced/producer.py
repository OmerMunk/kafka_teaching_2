from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')


for i in range(10):
    message = f'Bahur Ravak {i}'.encode('utf-8')
    producer.send('gur_topic', message)
    print(f'Sent {message}')

producer.flush() # producer.flush is used to make sure that all messages are sent before closing the producer
producer.close() # close the producer
