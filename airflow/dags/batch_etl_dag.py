from docker.types import Mount
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="batch_etl_dag",
    default_args=default_args,
    description="Run Spark batch ETL every 5 minutes",
    schedule_interval="*/5 * * * *",
    start_date=days_ago(0),   # ensures it starts from today
    catchup=False,
    is_paused_upon_creation=False,
    tags=["spark", "etl"],
) as dag:

    run_batch_job = DockerOperator(
        task_id="spark_batch_etl",
        image="spark-batch:latest",
        api_version="auto",
        auto_remove=True,               # removes container after completion
        command="spark-submit --master local[*] /app/batch_etl.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="clickstream",
        mount_tmp_dir=False,
        mounts=[
            Mount(source="spark_batch_code", target="/app", type="volume"),
            Mount(source="spark_data_volume", target="/app/data", type="volume"),
        ],
    )

    run_batch_job
