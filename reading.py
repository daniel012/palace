import pandas as pd
import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')

db_config = {
  'user': config['AWS']['User'],
  'password': config['AWS']['Password'],
  'host': config['AWS']['Address'],
  'database': config['AWS']['DB'],
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**db_config)

def extrac_data():
    query = "SELECT * FROM palace.bitso_trades order by tid limit 5000;"

    cursor = conn.cursor()
    data = pd.read_sql(query,conn)

    data = data.reindex(index=data.index[::-1])
    data.reset_index(inplace=True, drop=True)

    return data    

def sma(df, d):
    c = df.rolling(d).mean()
    return c.dropna() 


data = extrac_data()
data['mv20'] = sma(data.price, 10)
data['mv120'] = sma(data.price, 60)

print(data)
