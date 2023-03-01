import os
import psycopg2
import json

class SrealityPipeline:
    def __init__(self):
        '''
        ENV_HOSTNAME = os.getenv('HOSTNAME')
        ENV_DATABASE = os.getenv('DATABASE')
        ENV_PORT = os.getenv('PORT')
        ENV_USERNAME = os.getenv('USERNAME')
        ENV_PASSWORD = os.getenv('PASSWORD')
        '''
        
        ENV_HOSTNAME = 'db'
        ENV_DATABASE = 'sreality_db'
        ENV_PORT = '5432'
        ENV_USERNAME = 'postgres'
        ENV_PASSWORD = 'password'
        
        self.connection = psycopg2.connect(
            host=ENV_HOSTNAME,
            dbname=ENV_DATABASE,
            port=ENV_PORT,
            user=ENV_USERNAME,
            password=ENV_PASSWORD
        )

        self.cur = self.connection.cursor()

        self.cur.execute('DROP TABLE IF EXISTS flats')

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS flats (
                id SERIAL PRIMARY KEY,
                title TEXT,
                img_url TEXT,
                locality TEXT,
                price TEXT
            )
        ''')

        """
        self.cur.execute('''
            DELETE FROM flats *
        ''')
        """

    def process_item(self, item, spider):

        self.cur.execute(
            '''INSERT INTO flats (title, img_url, locality, price) values (%s,%s,%s,%s)''', (
            item['title'],
            item['img_url'],
            item['locality'],
            item['price']
        ))
        self.connection.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()