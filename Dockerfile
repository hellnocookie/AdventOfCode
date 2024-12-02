FROM python:3.12-slim

WORKDIR /app

# Install any needed packages
RUN pip install --no-cache-dir pytest

# Copy the project files
COPY . .

# Use shell as default command
CMD ["/bin/bash"] 