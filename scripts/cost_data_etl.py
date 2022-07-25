#!/usr/bin/env python

import psycopg2 as pg
from psycopg2.extras import execute_values
import requests
import sys
import os

def get_data():
    """Get CoinCap data"""
    try:
        r = requests.get("https://api.coincap.io/v2/assets", params = {'limit' : 10})
    except Exception as ex:
        print("There's been an issue connecting to API")
        sys.exit(1)
    return r.json()['data']

def connect_to_db():
    """Connect to database"""
    try:
        conn = pg.connect(host = os.getenv('DATABASE_HOST'), 
                          database = os.getenv('DATABASE_DB'), 
                          user = os.getenv('DATABASE_USER'), 
                          password = os.getenv('DATABASE_PASSWORD'), 
                          port = os.getenv('DATABASE_PORT'))
    except Exception as ex:
        print("There's been an issue connecting to database")
        sys.exit(1)
    return conn

def ingest_data(conn, data):
    cur = conn.cursor()
    columns = "id,rank,symbol,name,supply,max_supply,market_cap,volume_24hr,price,change_per_24hr,volume_we_24hr"
    query = "INSERT INTO crypto.assets ({}) VALUES %s".format(columns)
    values = [[value for value in coin.values()] for coin in data]
    execute_values(cur, query, values)
    conn.commit()

def remove_column(data):
    """Remove explorer key"""
    return [{k: v for k, v in d.items() if k != 'explorer'} for d in data]

def run():
    data = get_data()
    data = remove_column(data)
    conn = connect_to_db()
    ingest_data(conn, data)

if __name__ == "__main__":
    run()
    print("Updated")
