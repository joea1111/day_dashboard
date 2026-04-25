# Lab 13: Dockerfile for the WHOLE Monolith Project
FROM python:3.13.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install all project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install daphne channels django-filter drf-spectacular django-celery-beat djangorestframework-simplejwt requests

# Copy the entire project code
COPY . .

# Expose the port
EXPOSE 8000

# Migrate and start the server
# We use daphne because your project uses Channels/Real-time features
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 service_day_system.asgi:application"]
