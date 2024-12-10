# Real Time Data Pipeline Kafka Python MySQL PowerBI
This project showcases the development of a real-time data pipeline utilizing Apache Kafka for messaging, Python's `psutil` library for collecting system metrics, and MySQL for data storage. Furthermore, the collected metrics are visualized in real-time using Power BI, offering actionable insights into system performance.

## Technologies Used
- **Python:** Used for collecting system metrics via the `psutil` library and for interacting with Apache Kafka.
- **Apache Kafka:** A distributed streaming platform used to handle real-time data processing.
- **Apache Zookeeper:** Used for managing and coordinating Kafka brokers.
- **MySQL:** Stored and managed the collected metrics data in a relational database.
- **Power BI:** Used to create a real-time dashboard for visualizing the metrics data.

## Architecture
1. **Data Collection:** Python's `psutil` library collects system metrics such as CPU usage, memory usage, disk usage, and network activity.
2. **Data Production:** The collected metrics data is sent to Kafka topics via a Kafka producer.
3. **Data Consumption:** Kafka consumers read the messages from Kafka topics, process them, and load the data into a MySQL database.
4. **Dashboard Visualization:** Power BI connects to the SQL server database to visualize the real-time metrics in a user-friendly dashboard.

## Prerequisites
- Python 3.x
- Apache Kafka and Zookeeper
- SQL Server
- Power BI Desktop

## Repository Structure

```
Real-Time-Data-Pipeline-Kafka-Python-SQL server -PowerBI/
|-- dashboard/
|   |-- real_time_computer_performance.pbix
|-- Main/
|   |-- consumer.py
|   |-- data_pipeline.py
|   |-- producer.py
|   |-- requirements.txt
|   |-- sql-scripts.sql
|
|-- README.md
```
