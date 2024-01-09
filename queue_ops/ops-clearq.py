import os
from azure.storage.queue import QueueClient

try:
    print("Clearing queue")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.getenv('AZURE_STORAGE_QUEUE_NAME')

    queue_client = QueueClient.from_connection_string(connect_str, queue_name)

    # clear the queue
    queue_client.clear_messages()

    print("Queue cleared")


except Exception as ex:
    print('Exception:')
    print(ex)



