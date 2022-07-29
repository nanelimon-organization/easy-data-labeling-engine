import csv
import pandas as pd
from sqlalchemy import create_engine
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Create engine to connect with DB
def dummy():
    try:
        """engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=True)"""
        engine = create_engine(
            'postgres://ktbzsdryoagyfd:77e6db1cf7aeff73105c60b05327baab2510216f8fb7736f9f8b36cf005a284b@ec2-44-195-100-240.compute-1.amazonaws.com:5432/dem8vtnut4f7km',
            echo=True)
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
            df['label'] = df['label'].astype(object)
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


dummy()
