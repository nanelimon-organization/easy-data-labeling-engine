import csv
import pandas as pd
from sqlalchemy import create_engine
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Create engine to connect with DB
def dummy():
    try:
        #engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=True)
        engine = create_engine("postgresql://scibriigaxirvh" \
                                        ":701e929c57a1042d3ac1c53aa27a433ca0c15541329106abe1a012d00be8d533@ec2-107-22" \
                                        "-122-106.compute-1.amazonaws.com:5432/d9i8pr0r2k38vf ", echo=True)
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
