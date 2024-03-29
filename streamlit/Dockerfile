FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory inside the container
WORKDIR /streamlit

# Copy the rest of the app
COPY . /streamlit

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set the command to run the uvicorn server
CMD CMD ["streamlit", "run", "streamlit_app.py"]