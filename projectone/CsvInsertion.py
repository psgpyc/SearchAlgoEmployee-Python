import csv
import psycopg2

conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")
cur = conn.cursor()


def insert_csv(csvval):

    with open(csvval, 'r') as f:
        count = 0
        reader = csv.reader(f)
        next(reader)  # Skipping the header row.
        for row in reader:
            if len(row) != 0:

                cur.execute(
                    "INSERT INTO userdetails(name,email,phone,bio,dob,gender,address,long,lat,SocialMedia) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)",
                    row)
                count += 1
                print(f"inserted row: {count}")
        conn.commit()



