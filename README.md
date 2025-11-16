# 🚀 Real-Time & Batch ETL Pipeline with Kafka, PySpark, MySQL & Airflow

This project is a complete **end-to-end data engineering pipeline** built using Docker. It includes:

* **Kafka Producer & Consumer** (real-time streaming)
* **PySpark Streaming** for real-time transformations
* **PySpark Batch ETL** jobs
* **MySQL** for storage
* **Airflow** for orchestrating batch jobs
* **Zookeeper + Kafka Broker** setup with health checks
* **Shared Volumes** for seamless data exchange between streaming and batch components

---

## 📌 Architecture Overview

The project implements both **real-time streaming** and **batch ETL processing** using a shared data pipeline:

```
Kafka Producer → Kafka Broker → PySpark Streaming → Clean Data (Volume)
                                             ↓
                                     PySpark Batch ETL → Aggregated Output
                                             ↓
                                           MySQL
                                    Airflow Scheduler
```

## ▶️ How to Run the Project

### Step 1: Build & Start All Services

```bash
docker-compose up -d --build
```

### Step 2: Check Status of Services

```bash
docker ps
```

### Step 3: Check Airflow UI

```
http://localhost:8081
```

### Step 4: MySQL DB Access

* Host: `localhost`
* Port: `33060`
* User: `root`
* Password: `password`

### Step 5: Kafka

* Broker: `kafka:9092`

---

## 📊 Data Flow Explanation

### **Producer → Kafka**

Producer sends JSON messages into a Kafka topic.

### **Kafka → PySpark Streaming**

The consumer reads Kafka events and cleans/transforms them.
The results go into:

```
/app/data/clean/
```

(shared through volume `spark_data_volume`)

### **PySpark Batch Jobs**

Runs periodically via Airflow:

```
/app/data/aggregates/
```

### **MySQL Storage**

Batch results OR consumer data can be saved to MySQL.

---

## 🔧 Volumes Used

| Volume Name         | Purpose                                                         |
| ------------------- | --------------------------------------------------------------- |
| `spark_batch_code`  | Shares batch ETL code between Airflow & PySpark batch container |
| `spark_data_volume` | Shares cleaned streaming output & checkpoints                   |


---

## 🧹 Cleanup

```bash
docker-compose down -v
```
