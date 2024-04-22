import os
import psycopg2
from psycopg2 import Error

conectionString = "postgresql://charly1616:3saw59-hTh8ZeR4-BIc9zQ@transport-db-13923.7tt.aws-us-east-1.cockroachlabs.cloud:26257/TRANSPORT_DataBase?sslmode=verify-full"



def create_table():
    try:
        conn = psycopg2.connect(conectionString)
        cursor = conn.cursor()
        
        u = 'CharlyMaster'
        c = "CUCARACHACUCARACHA"
        querryCreatTab = "UPSERT INTO Administrador_User (Admin_User, Admin_Passw) VALUES (%s,%s)"
        #cursor.execute(querryCreatTab,(u,c))
        cursor.execute("SELECT * FROM ADMINISTRADOR_USER")
        #cursor.execute("DELETE FROM ADMINISTRADOR_USER")
        v = cursor.fetchall()
        print(v)
        conn.commit()
        cursor.close
    except (Exception, Error) as error:
        print(error)


create_table()
