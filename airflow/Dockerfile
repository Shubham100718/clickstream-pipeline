# Use the official Airflow image
FROM apache/airflow:2.9.0

# Switch to root only to install system-level packages
USER root

# Install MySQL development libs for mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Switch back to airflow user for pip install
USER airflow

# Install mysqlclient as airflow user
RUN pip install --no-cache-dir mysqlclient

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# Switch to root user to execute entrypoint
USER root

# Make entrypoint executable
RUN chmod +x /entrypoint.sh

# Match the Docker group inside container with host GID
ARG DOCKER_GID=984
# Add airflow user to Docker group inside container
RUN groupadd -g ${DOCKER_GID} docker || true && usermod -aG docker airflow

# Switch back to airflow user
USER airflow

# Set default entrypoint
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
