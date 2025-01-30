import os
from azure.storage.queue import QueueClient

try:
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.getenv('AZURE_STORAGE_QUEUE_NAME')

    queue_client = QueueClient.from_connection_string(connect_str, queue_name)

    print("Queue length: " + str(queue_client.get_queue_properties().approximate_message_count))

except Exception as ex:
    print('Exception:')
    print(ex)



