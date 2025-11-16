# Use the official Zookeeper image
FROM confluentinc/cp-zookeeper:7.6.0

# Switch to root to install additional packages
USER root

# Install additional zookeeper healthcheck dependencies
RUN microdnf install -y nc && microdnf clean all

# Switch back to app user (non-root for safety)
USER appuser
