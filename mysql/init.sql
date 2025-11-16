CREATE DATABASE IF NOT EXISTS airflow_db;
CREATE DATABASE IF NOT EXISTS clickdb;

USE clickdb;

CREATE TABLE IF NOT EXISTS daily_page_views (
  date DATE NOT NULL,
  country VARCHAR(100),
  page_views INT,
  PRIMARY KEY (date, country)
);
