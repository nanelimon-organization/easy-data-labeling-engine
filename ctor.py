import csv
import pandas as pd
from sqlalchemy import create_engine
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Create engine to connect with DB
def dummy():
    try:
        """engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=True)"""
        engine = create_engine('postgresql://tfebtxzxlgssjc:41e1741c907c8fa23d960f7c99b53cc83688da12337f4565dde9d9e51c96f899@ec2-54-225-234-165.compute-1.amazonaws.com:5432/da5jjovb79fk6g', echo=True)
        print('Engine created!')
    except Exception as ex:
        print("Can't create 'engine", ex)
    else:
        # Get data from CSV file to DataFrame(Pandas)
        with open('static/datas/data.csv', newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            columns = [
                'id',
                'text',
                'label',
                'tagging_status'
            ]
            df = pd.DataFrame(data=reader, columns=columns)
            # Dataframe editing.
            df['id'] = df['id'].astype(int)
            df['label'] = df['label'].astype(bool)
            df['tagging_status'] = df['tagging_status'].astype(bool)
            df['tagging_status'] = df['tagging_status'].ffill()
            print(df.head(15))
            df = df.sample(n=10000)
        # Standart method of Pandas to deliver data from DataFrame to Database table.
        try:
            # load the data into a Pandas DataFrame
            with engine.begin() as connection:
                df.to_sql('scraped', con=connection, if_exists='replace')
                print('Done, ok!')
        except Exception as ex:
            print('Something went wrong!', ex)
