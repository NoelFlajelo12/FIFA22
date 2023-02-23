import pandas as pd
import os
import mysql.connector
from sqlalchemy import create_engine

ruta=os.getcwd()

df_jugadores = pd.read_csv(ruta +"\\fifa20\\players_20.csv", sep=",")
df_equipos = pd.read_csv(ruta+"\\fifa20\\teams_and_leagues.csv", sep=",")

print("¿Hay valores nulos?")
print(df_jugadores.isnull().values.all())

del df_jugadores['sofifa_id']
del df_jugadores['player_url']
del df_jugadores['ls']
del df_jugadores['st']
del df_jugadores['rs']
del df_jugadores['lw']
del df_jugadores['lf']
del df_jugadores['cf']
del df_jugadores['rf']
del df_jugadores['rw']
del df_jugadores['lam']
del df_jugadores['cam']
del df_jugadores['ram']
del df_jugadores['lm']
del df_jugadores['lcm']
del df_jugadores['cm']
del df_jugadores['rcm']
del df_jugadores['rm']
del df_jugadores['lwb']
del df_jugadores['ldm']
del df_jugadores['cdm']
del df_jugadores['rdm']
del df_jugadores['rwb']
del df_jugadores['lb']
del df_jugadores['lcb']
del df_jugadores['cb']
del df_jugadores['rcb']
del df_jugadores['rb']


#conexion con el servidor
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
)

#creación del cursor
cursor = conexion.cursor()

#creación de nueva base de datos
cursor.execute("DROP DATABASE IF EXISTS FIFA;")
cursor.execute("CREATE DATABASE FIFA;")

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="root",
                               db="fifa"))

df_jugadores.to_sql('fifa20', engine, chunksize=500000,
          method='multi', index=False, if_exists='append')
