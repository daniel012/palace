"""
created: jesus oliveros

"""

from datetime import datetime
import pandas as pd
import requests
import sqlalchemy as sql
from sqlalchemy.sql.expression import join
from datetime import datetime
import time 
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')


def extracBitsoapi():
    response  = requests.get(config['Bitso']['domain']+'trades/?book=btc_mxn')
    json_response = response.json()
    datos = json_response['payload']
    df = pd.DataFrame(datos)
    engine = sql.create_engine('mysql+pymysql://'+config['AWS']['User']+':'+config['AWS']['Password']+'@'+config['AWS']['Address']+'/'+config['AWS']['DB'])

    initial_q = """INSERT  INTO bitso_trades
    (book, created_at , amount, maker_side, price, tid)
    VALUES
    """
    values_q = ",".join(["""('{}','{}','{}','{}','{}','{}')""".format(
        row.book, 
        row.created_at,
        row.amount, 
        row.maker_side, 
        row.price,
        row.tid) for idx, row in df.iterrows()])

    end_q ="""
        ON DUPLICATE KEY UPDATE 
            book = values(book),
            created_at = values(created_at) ,
            amount = values(amount) ,
            maker_side = values(maker_side), 
            price = values(price) ,
            tid = values(tid);
    """

    query = initial_q + values_q + end_q

    engine.execute(query)
    return

while True:
   extracBitsoapi()
   print('act BD a  las {} con'.format(datetime.now()))
   time.sleep(15)
