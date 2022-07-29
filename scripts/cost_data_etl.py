#!/usr/bin/env python
import psycopg2 as pg
from psycopg2.extras import execute_values
from datetime import datetime, timezone
import requests
import sys
import os

def get_data():
    """Get CoinCap data"""
    coin_list = ['bitcoin','ethereum','cosmos','solana','algorand','polygon','uniswap','dogecoin','litecoin','polkadot']
    payload = {"ids" : ','.join(coin_list)}
    try:
        r = requests.get("https://api.coincap.io/v2/assets", params = payload)
    except Exception as ex:
        print("There's been an issue connecting to API")
        sys.exit(1)
    return r.json()['data']

def connect_to_db():
    """Connect to database"""
    try:
        conn = pg.connect(host = os.getenv('DATABASE_HOST', default = "warehouse"), 
                          database = os.getenv('DATABASE_DB'), 
                          user = os.getenv('DATABASE_USER'), 
                          password = os.getenv('DATABASE_PASSWORD'), 
                          port = os.getenv('DATABASE_PORT'))
    except Exception as ex:
        print(f"There's been an issue connecting to database: {ex}")
        sys.exit(1)
    return conn

def ingest_data(conn, data):
    """Load data into database"""
    cur = conn.cursor()
    columns = ['id','rank','symbol','name','supply','max_supply','market_cap','volume_24hr','price','change_per_24hr', 'volume_we_24hr', 'update_utc']
    columns = ','.join(columns)
    query = "INSERT INTO crypto.assets ({}) VALUES %s".format(columns)
    values = [[value for value in coin.values()] for coin in data]
    try:
        execute_values(cur, query, values)
    except Exception as ex:
        print(f"There was an issue inserting data in db: {ex}")
        sys.exit(1)
    conn.commit()

def remove_explorer_key(data):
    """Remove Explorer Key from Data if exists"""
    return [{k: v for k, v in d.items() if k != 'explorer'} for d in data]

def add_utc_time_key(data):
    """Added current UTC time to Data"""
    now = datetime.now(timezone.utc)
    return [dict(d, **{'update_utc' : now}) for d in data]

def run():
    data = get_data()
    data = add_utc_time_key(data)
    data = remove_explorer_key(data)
    conn = connect_to_db()
    ingest_data(conn, data)

if __name__ == "__main__":
    run()
    print(f"Update Successful at {datetime.now(timezone.utc)} utc")