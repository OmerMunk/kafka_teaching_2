# Kafka architecture
"""
- Brokers - server that store and forward messages
- Topics - Categories or feed names that the messages are published to
- Partition - splits of a topic for parallelism
- Producers and Consumers - applications that write data to and read from kafka
- zookeeper - service that coordinates kafka brokers
"""


# pull the kafka image:
# docker pull apache/kafka:3.9.0

# start the kafka container:
# docker run -p 9092:9092 apache/kafka:3.9.0

# pip install kafka-python

