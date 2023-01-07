FROM python:3.9.12

# this disables an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# this disables the creation of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This ensures that django output will not be buffered by by docker
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy cd to /app
COPY . .