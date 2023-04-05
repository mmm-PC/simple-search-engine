from src.database.connection import connect_to_db
import csv
import json
import datetime

def parse_to_db(filepath):

    format = '%Y-%m-%d %H:%M:%S'
    connection = connect_to_db()

    with open(filepath,'r', encoding='UTF8') as csvfile, connection.cursor() as cursor:
        csv_reader = csv.reader(csvfile, delimiter=',')
        
        for row in csv_reader:
            text = row[0]
            try:
                created_date = datetime.datetime.strptime(row[1], format)
            except:
                print("incorrect date format, skipping row...")
                continue

            try:
                rubrics = json.loads(row[2].replace("'",'"'))
            except:
                print("rubrics array is corrupted, skipping row...")
                continue

            cursor.execute("INSERT INTO posts (rubrics, text, created_date) VALUES (ARRAY{2},'{0}','{1}')".format(text.replace("'","''"), created_date, rubrics))

    connection.commit()

    cursor.close()
    connection.close()
    
if __name__ == "__main__":
    parse_to_db("database\\data\\posts.csv")