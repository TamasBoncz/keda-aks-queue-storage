import os
import logging
from azure.storage.queue import QueueClient

logging.basicConfig(level=logging.INFO)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    try:
        logging.info("Running...")
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        queue_name = os.getenv('AZURE_STORAGE_QUEUE_NAME')

        if not connect_str or not queue_name:
            logging.error("Environment variables for connection string or queue name are not set")
            return

        queue_client = QueueClient.from_connection_string(connect_str, queue_name)

        try:
            # get next message from the queue
            message_full = queue_client.receive_message(visibility_timeout=300)  # hides the message from the queue for 5 minutes

            if message_full is None:
                logging.info("No messages in the queue")
                return

            message = message_full.content
        except Exception as ex:
            logging.exception("Exception occurred while receiving message")
            return

        try:
            logging.info(f"Calculating fibonacci number for {message}")
            message = int(message)
            result = fibonacci(message)
            logging.info(f"Fibonacci result: {result}")

            # delete message from the queue
            queue_client.delete_message(message_full)
            logging.info("Message processed and deleted from the queue")
        except Exception as ex:
            logging.exception("Exception occurred while processing message")
            return

    except Exception as ex:
        logging.exception("Exception occurred in main function")
        return

if __name__ == "__main__":
    main()



