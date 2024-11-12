
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

targets = {}
count = 0
for message in consumer:
    target = message.value.decode('utf-8')
    target_tuple = eval(target)
    target_id, target_x, target_y = target_tuple
    if target_id not in targets:
        targets[target_id] = {
            "distance": 0,
            "locations": []
        }
    targets[target_id]['locations'].append((target_x, target_y))
    target_locations_count = len(targets[target_id]['locations'])
    if target_locations_count > 1:
        last_location = targets[target_id]['locations'][-2]
        new_location = targets[target_id]['locations'][-1]
        distance = ((new_location[0] - last_location[0]) ** 2 + (new_location[1] - last_location[1]) ** 2) ** 0.5
        targets[target_id]['distance'] += distance
    count+=1
    print(count)
    if count == 900000:
        print(targets[1])
        break


