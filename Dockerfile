# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

# Download and install the 'en_core_web_sm' model
RUN python -m spacy download en_core_web_sm

# Copy the rest of the application's code into the container
COPY . .

# Install Python packages
#RUN pip install .

# Expose a port for possible future use
EXPOSE 9000

# Command to run the FastAPI app with Uvicorn
#CMD ["uvicorn", "cleanmydata.app:app", "--host", "0.0.0.0", "--port", "9000"]

# Using CMD to use the environment variable PORT provided by railway.app
CMD ["uvicorn", "cleanmydata.app:app", "--host", "0.0.0.0", "--port", "${PORT:-9000}"]