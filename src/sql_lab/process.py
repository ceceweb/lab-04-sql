"""Read, clean, and load MOCK_DATA.csv into a MySQL table."""

import logging
import os
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]

def read_data(filename):
	"""Load a CSV file into a pandas DataFrame and return it."""
	logger.info("Reading %s", filename)
	df = pd.read_csv(filename)
	logger.info("Read %d rows", len(df))
	return df

def clean_data(data):
	"""Remove rows with missing values, convert dates to datetime, and return the cleaned dataframe"""
	logger.info("Cleaning data")
	data = data.dropna().copy()
	data["movein_date"] = pd.to_datetime(data["movein_date"],)
	logger.info("%d rows remain after cleaning", len(data))
	return data

def load_data(data, table):
	"Create the table if needed and insert each DataFrame row into it."""
	engine = None
	try:
		url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}"
		engine = create_engine(url)
		data.to_sql(table, engine, if_exists="replace", index=False)
		logger.info("Inserted %d rows into %s", len(data), table)
	except Exception as err:
		logger.error("Database error: %s", err)
	finally: 
		if engine:
			engine.dispose()

def main():
	"""Run the read, clean, and load steps in order."""
	data = read_data("MOCK_DATA.csv")
	data = clean_data(data)
	load_data(data, "mock")

if __name__ == "__main__":
	main()
