#!/bin/bash
set -e

# Wait for MySQL to be ready
echo "Waiting for MySQL..."
while ! nc -z mysql_db 3306; do
  sleep 2
done
echo "MySQL is ready!"

# Initialize Airflow DB only if not already initialized
if [ ! -f "/opt/airflow/airflow.db.init" ]; then
  echo "Initializing Airflow database..."
  airflow db init
  touch /opt/airflow/airflow.db.init

  echo "Creating Airflow admin user..."
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname user \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Start scheduler in background
echo "Starting Airflow scheduler..."
airflow scheduler &
SCHEDULER_PID=$!

# Wait 15 seconds so scheduler loads DAGs
echo "Waiting for scheduler to parse DAGs..."
sleep 15

# Start webserver (foreground)
echo "Starting Airflow webserver..."
exec airflow webserver
