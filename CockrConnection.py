from sqlalchemy import create_engine, text
import psycopg2

conn = psycopg2.connect("postgresql://charly1616:3saw59-hTh8ZeR4-BIc9zQ@transport-db-13923.7tt.aws-us-east-1.cockroachlabs.cloud:26257/TRANSPORT_DataBase?sslmode=verify-full")
#GRANT INSERT ON TABLE TTT TO charly1616;

with conn.cursor() as cur:
    try:

        cur.execute("UPSERT INTO TTT VALUES (45, 46, 47);")
        cur.execute("SELECT * FROM TTT;")
        res = cur.fetchall()
        conn.commit()
        print(res)
    except Exception as e:
        print('Hubo un error:', e)
        print('No hubo respuesta')
