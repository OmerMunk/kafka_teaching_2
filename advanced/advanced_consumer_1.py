import time

from kafka import KafkaConsumer

# consumer groups - קבוצות צרכנים
# a group of consumers that share the same group id
# קבוצת צרכנים שחולקים את אותו מזהה ייחודי
# purpose: allow load balancing for message concunmption
# מטרה: מאפשר חלוקת עומס בין צרכנים של אותו טופיק.


consumer1 = KafkaConsumer(
    'gur_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='group1'
)


for message in consumer1:
    print(f"CONSUMER 1 received message: {message.value.decode('utf-8')}")
    time.sleep(2)
    consumer1.commit()