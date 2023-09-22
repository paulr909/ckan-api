# encoding: utf-8
#!/usr/bin/env python3
import os
import pyodbc
import csv
from decouple import config
from time import gmtime, strftime

SERVER = "tcp:sqlserver.ckan.company_name.internal"
DATABASE = "ckan"
USER = "company_name_ckan"
PASSWORD = config("PASSWORD")


def connect_db():
    file_path = "dataset/bitcoin-market-price.csv"
    connect = None

    if os.path.exists(file_path):

        try:
            connect = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                + SERVER
                + ";DATABASE="
                + DATABASE
                + ";UID="
                + USER
                + ";PWD="
                + PASSWORD
            )

        except pyodbc.Error as e:
            print(e.args[1])
            print("Database connection unsuccessful")
            quit()

        cursor = connect.cursor()

        sql_select = "SELECT FROM [bitcoin_market_price] ORDER BY [date]"

        try:
            cursor.execute(sql_select)
            # Fetch the data returned
            results = cursor.fetchall()
            # Extract the table headers
            headers = [i[0] for i in cursor.description]

            csv_from_sql = csv.writer(
                open(file_path, "w", newline=""),
                delimiter=",",
                lineterminator="\r\n",
                quoting=csv.QUOTE_NONE,
                escapechar="\\",
            )

            csv_from_sql.writerow(headers)
            csv_from_sql.writerows(results)
            print("Data export successful")

        except pyodbc.Error as e:
            print("Data export unsuccessful")
            quit()

        finally:
            connect.close()

    else:
        print("File path does not exist")

    print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


if __name__ == "__main__":
    connect_db()
