"""
created: jesus oliveros

"""

import pandas as pd
import sqlalchemy as sql
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')

engine = sql.create_engine('mysql+pymysql://'+config['AWS']['User']+':'+config['AWS']['Password']+'@'+config['AWS']['Address']+'/'+config['AWS']['DB'])

def execute_query(query ):
    engine.execute(query)
    return
