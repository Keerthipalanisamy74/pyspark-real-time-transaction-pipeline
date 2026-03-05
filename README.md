# Simulated Real-Time Transaction Data Pipeline using PySpark

## Project Overview
This project simulates a real-time transaction data pipeline using PySpark Structured Streaming. The pipeline processes streaming transaction data, performs cleaning and transformation, detects high-value transactions, and calculates revenue metrics.

## Business Problem
Financial institutions process thousands of transactions every second. This project demonstrates how streaming technologies can process transaction data in real time and detect important insights.

## Technologies Used
- Python
- PySpark
- Spark Structured Streaming
- SQL
- Parquet

## Features
- Real-time transaction processing
- Window-based revenue aggregation
- High-value transaction detection
- Fault tolerant pipeline with checkpointing
- Parquet data storage

## Project Architecture
Data Generator → PySpark Streaming → Data Processing → Aggregation → Parquet Storage

## Project Structure

pyspark-real-time-transaction-pipeline
│
├── data_generator.py
├── streaming_pipeline.py
├── requirements.txt
└── README.md
