# Lab 13 Task 3.2: Dockerfile - Deploy NGO Microservice
FROM python:3.13.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install only the dependencies needed for the microservice
RUN pip install django djangorestframework django-filter drf-spectacular requests

# Copy the microservice code
COPY microservices/ngo_service/ .

# Expose the port
EXPOSE 8000

# Migrate and run
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
