# encoding: utf-8
#!/usr/bin/env python3
import psycopg2
from decouple import config
from time import gmtime, strftime


def connect():
    conn = None
    try:
        print("Connecting to the PostgreSQL database")
        conn = psycopg2.connect(
            host=config("DATASTORE_HOST"),
            database=config("DATASTORE_DATABASE"),
            user=config("DATASTORE_USER"),
            password=config("DATASTORE_PASSWORD"),
            port=config("DATASTORE_PORT"),
        )

        cur = conn.cursor()

        cur.execute(
            'TRUNCATE TABLE public."249f32e0-504c-425f-aa78-73006004baf7" RESTART IDENTITY;'
        )

        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Dataset truncated successfully")
            print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


if __name__ == "__main__":
    connect()
