import json
from kafka import KafkaConsumer
import mysql.connector
from mysql.connector import Error
from datetime import datetime


def consum():
    # Kafka broker configuration
    bootstrap_servers = 'localhost:9092'
    topic = 'firstTopic'

    # Create a Kafka consumer
    consumer = KafkaConsumer(topic,
                             group_id='my_consumer_group',
                             bootstrap_servers=bootstrap_servers,
                             value_deserializer=lambda x: x.decode('utf-8'))

    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            database='system_performance',  
            user='root',                    
            password=''                     
        )

        if connection.is_connected():
            print("Connexion SQL réussie.")
            cursor = connection.cursor()

            for message in consumer:
                try:
                    # Split the message value into individual values
                    values = message.value.split(',')
                    # Unpack the values into variables
                    current_datetime, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage = values

                    # Extract datetime without milliseconds
                    formatted_datetime = current_datetime.split('.')[0]

                    # Format current_datetime to the correct format for MySQL
                    formatted_datetime = datetime.strptime(formatted_datetime, '%Y-%m-%d %H:%M:%S')

                    # Insert data into MySQL database
                    insert_query = """INSERT INTO performance 
                                    (time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, 
                                     memory_free, bytes_sent, bytes_received, disk_usage)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    data_to_insert = (
                        formatted_datetime, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free,
                        bytes_sent, bytes_received, disk_usage)
                    cursor.execute(insert_query, data_to_insert)
                    connection.commit()

                    print(f"Inserted at {formatted_datetime} into the database.")
                    print("-------------------")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue

    except Error as e:
        print(f"Erreur lors de la connexion MySQL : {e}")
        connection = None
        cursor = None

    finally:
        if connection is not None and cursor is not None:
            # Close connections
            cursor.close()
            connection.close()
            print("Consumer and database connections closed.")

