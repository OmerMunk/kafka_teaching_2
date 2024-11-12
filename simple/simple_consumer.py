
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'gur_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

# first parameter is the topic to listen to / subscribe
# second parameter (bootstrap_servers) = the address of the kafka server
# third parameter (auto_offset_reset) = where to start reading the messages from
# fourth parameter (enable_auto_commit) = whether to commit the offset automatically
# fifth parameter (group_id) = the group id of the consumer