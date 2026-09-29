"""Query the mock table in yvw3nq_mock and demonstrate the results"""

import logging
import os
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]

def get_data_by_group(value):
	"""Return all rows from mock where the 'group' column equals value"""
	conn = None
	try:
		conn = mysql.connector.connect(
			host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME
		)
		cursor = conn.cursor()
		query = "SELECT * FROM mock WHERE 'group' = %s;"
		cursor.execute(query, (value,))
		results = cursor.fetchall()
		logger.info("Fetched %d rows where group = %s", len(results), value)
		return results
	except mysql.connector.Error as err:
		logger.error("Database erro: %s", err)
		return None
	finally:
		if conn and conn.is_connected():
			conn.close()

def plot_counts(groupby):
	"""Count rows per distinct value of groupby, show a bar chart, and return the DataFrame. """
	conn = None
	try:
		conn = mysql.connector.connect(
			host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME
		)
		cursor = conn.cursor()
		query = f"SELECT '{groupby}', COUNT(*) FROM mock GROUP BY '{groupby}';"
		cursor.execute(query)
		results = cursor.fetchall()
		logger.info("Counted rows for %d distinct values of %s", len(results), groupby)
		
		df = pd.DataFrame(results, columns=[groupby, 'count'])
		df.plot.bar(x=groupby, y="count", legend=False)
		plt.show()
		return df
	except mysql.connector.Error as err:
		logger.error("Database error: %s", err)
		return None
	finally:
		if conn and conn.is_connected():
			conn.close()

def main():
	"""Run the demo queries and print/show their results"""
	print("=== rows in group Dins ===")
	print(get_data_by_group("Dins"))

	print("=== counts by group ===")
	plot_counts("group")

if __name__ == "main":
	main()
