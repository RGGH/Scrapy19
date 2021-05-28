#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import sys
import psycopg2

class JobzPipeline:

    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        # connect to Connect to DB
        try:
            self.conn = psycopg2.connect(
                                    user = 'user3',
                                    password = 'password3',
                                    host = '192.168.1.9',
                                    port=5432,
                                    database = 'jobs'
                                    )
            # create a cursor
            self.curr = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    # Allow enough varchar for long urls
    # posted will come from 
    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS listings (
            id serial,
            url VARCHAR(190),
            description text,
            posted  date
            )
            """)

    def process_item(self, item, spider):
        self.store_db(item)

    def store_db(self,item):

        url=item.get('url'),
        description=item.get('description'),
        posted=item.get('posted')
        vals = (url,description,posted)

        # insert multiple rows of jobs data
        sql = """
            INSERT INTO listings (url,description, posted) VALUES(%s,%s,%s)
            """
        try:
            self.curr.execute(sql,vals)
            self.conn.commit()
        except:
            pass
            


    def close_spider(self, spider):     
        self.conn.close()


