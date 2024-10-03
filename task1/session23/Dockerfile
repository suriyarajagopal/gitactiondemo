# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Flask package
RUN pip install Flask

# Expose port 5000 to allow communication to/from the container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
