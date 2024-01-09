# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

COPY pycontainer.py /app

# Install any needed packages
RUN pip install --no-cache-dir azure-storage-queue

# Run pycontainer.py when the container launches
CMD ["python", "pycontainer.py"]