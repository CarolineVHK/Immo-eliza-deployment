FROM python:3.9.6


# Copy the rest of the app
COPY . /app

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set the command to run the uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]