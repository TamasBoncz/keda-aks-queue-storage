from azure.storage.queue import QueueClient
import os

try:
    print("Running...")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.getenv('AZURE_STORAGE_QUEUE_NAME')

    queue_client = QueueClient.from_connection_string(connect_str, queue_name)

    try:
        # get next message from the queue      
        message_full = queue_client.receive_message(visibility_timeout=300) # hides the message from the queue for 5 minutes
        # print(message_full)
        
        if message_full is None:
            print("No messages in the queue")
            exit(0)

        message = message_full.content
    except Exception as ex:
        print('Exception:')
        print(ex)
        exit(1)

    try:
        print("Calculating fibonacci number for " + message)
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return (fibonacci(n-1) + fibonacci(n-2))
        
        message = int(message)
        print(fibonacci(message))

        # delete message from the queue
        queue_client.delete_message(message_full)
        print("Message processed and deleted from the queue")
        exit(0)
    
    except Exception as ex:
        print('Exception:')
        print(ex)
        exit(1) 


except Exception as ex:
    print('Exception:')
    print(ex)
    exit(1)



