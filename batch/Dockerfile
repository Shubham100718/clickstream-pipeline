# Use the official Apache Spark image
FROM apache/spark:3.5.1

# temporarily switch to root
USER root

# Set working directory
WORKDIR /app

# Copy your app files
COPY . /app

# Install all required dependencies
RUN pip install --no-cache-dir pyspark mysql-connector-python loguru

# Install MySQL JDBC driver for Spark
RUN wget -q https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-8.3.0.tar.gz -O /tmp/mysql-connector.tar.gz && \
    tar -xzf /tmp/mysql-connector.tar.gz -C /tmp && \
    cp /tmp/mysql-connector-j-8.3.0/mysql-connector-j-8.3.0.jar /opt/spark/jars/

# switch back to spark user (for safety)
USER spark

# Run your Spark job
CMD ["spark-submit", "--master", "local[*]", "batch_etl.py"]
