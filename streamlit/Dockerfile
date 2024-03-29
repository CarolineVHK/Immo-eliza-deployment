FROM python:3.9.6

# Set the working directory inside the container
WORKDIR /streamlit

# Copy the rest of the app
COPY . /streamlit

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Set the command to run the uvicorn server
CMD ["streamlit", "run", "homepage.py"]