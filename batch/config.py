# Config for batch ETL job
INPUT_PATH = "/app/data/clean/"
OUTPUT_PATH = "/app/data/aggregates/"
JDBC_URL = "jdbc:mysql://mysql_db:3306/clickdb"  # use service name, not localhost
DB_TABLE = "daily_page_views"
DB_USER = "root"
DB_PASSWORD = "password"
