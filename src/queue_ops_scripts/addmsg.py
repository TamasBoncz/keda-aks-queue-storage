import random, os
from azure.storage.queue import QueueClient

try:
    print("Adding messages to the queue")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.getenv('AZURE_STORAGE_QUEUE_NAME')

    queue_client = QueueClient.from_connection_string(connect_str, queue_name)

    # add messages to the queue
    for i in range(100):
        msg = random.randint(35, 42)
        queue_client.send_message(msg)

    print("Messages added to the queue")
    print("New queue length: " + str(queue_client.get_queue_properties().approximate_message_count))


except Exception as ex:
    print('Exception:')
    print(ex)



