import pandas as pd
import os
import mysql.connector
from sqlalchemy import create_engine

ruta=os.getcwd()

df_jugadores = pd.read_csv(ruta +"\\fifa20\\players_20.csv", sep=",")
df_equipos = pd.read_csv(ruta+"\\fifa20\\teams_and_leagues.csv", sep=",")

del df_jugadores['sofifa_id']
del df_jugadores['player_url']
del df_jugadores['loaned_from']
del df_jugadores['real_face']
del df_jugadores['body_type']
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
          method='multi', index=False, if_exists='replace')

df_jugador = df_jugadores[['short_name','long_name','age','dob','height_cm','weight_kg','nationality','club','overall','player_positions']].copy()
df_jugador.to_sql('jugador', engine, chunksize=500000,
          method='multi', index=False, if_exists='replace')

df_club = df_jugadores[['club','team_position','team_jersey_number' ]].copy()
df_club.to_sql('club', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')
            
df_nacionalidad = df_jugadores[['nationality','nation_position','nation_jersey_number' ]].copy()
df_nacionalidad.to_sql('nacionalidad', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')

df_habilidad = df_jugadores[['overall','potential','international_reputation','skill_moves','weak_foot', 'work_rate']].copy()
df_habilidad.to_sql('habilidad', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')

df_habilidad_jugador = df_jugadores[['player_positions','pace','shooting','passing','dribbling','defending','physic']].copy()
df_habilidad_jugador.to_sql('habilidad_jugador', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')

df_habilidad_portero = df_jugadores[['player_positions','gk_diving','gk_handling','gk_kicking','gk_reflexes','gk_speed','gk_positioning']].copy()
df_habilidad_portero.to_sql('habilidad_portero', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')

df_fisico = df_jugadores[['height_cm','weight_kg','attacking_heading_accuracy','movement_agility','movement_reactions','power_jumping','power_strength','power_stamina']].copy()
df_fisico.to_sql('altura', engine, chunksize=500000,
            method='multi', index=False, if_exists='replace')

