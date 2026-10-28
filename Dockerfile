# Use a specific Python version
FROM python:3.12.10-slim

# Set the working directory
WORKDIR /app

# Create a non-root user for security
RUN useradd --create-home appuser

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Banking App files
COPY --chown=appuser:appuser app.py .

# Run the application as a non-root user
USER appuser

# Document the application port
EXPOSE 5090

# Start the Banking App
CMD ["python", "app.py"]
