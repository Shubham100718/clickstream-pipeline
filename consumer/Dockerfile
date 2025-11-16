# Use the official Apache Spark image
FROM apache/spark:3.5.1

# Switch to root to install additional packages
USER root

# Set working directory
WORKDIR /app

# Copy your app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir pyspark loguru

# Install Spark-Kafka dependencies 
RUN wget -P /opt/spark/jars/ \
    -q https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar && \
    wget -P /opt/spark/jars/ \
    -q https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar && \
    wget -P /opt/spark/jars/ \
    -q https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.1/kafka-clients-3.5.1.jar && \
    wget -P /opt/spark/jars/ \
    -q https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar

# Create writable data directory for Spark
RUN mkdir -p /app/data && chmod -R 777 /app/data

# Switch back to spark user (non-root for safety)
USER spark

# Run your Spark job
CMD ["spark-submit", "--master", "local[*]", "streaming_consumer.py"]
