"""
created: jesus oliveros

"""

import pandas as pd
import requests
import sqlalchemy as sql
from sqlalchemy.sql.expression import join

response  = requests.get('https://api.bitso.com/v3/trades/?book=btc_mxn')
json_response = response.json()
datos = json_response['payload']
df = pd.DataFrame(datos)

engine = sql.create_engine('mysql+pymysql://admin:1234689h0lA@palace.cluster-cnnnw4vopgyu.us-east-2.rds.amazonaws.com/palace')

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

# print(query)