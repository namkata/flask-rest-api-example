# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /src

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Set environment variables, if needed
# ENV FLASK_APP=main.py
# ENV FLASK_ENV=development

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
