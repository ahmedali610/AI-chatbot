# Use an official Python image as a base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend files
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
