#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:12:16 2018

@author: marcelolaprea
"""
import MySQLdb
import pandas as pd

class MySQLConnection:
    
    def __init__(self, host, user, passw, dataBaseName):
        self.host = host
        self.user = user
        self.passw = passw 
        self.dataBaseName = dataBaseName
    
    #Funcion para crear el DataFrame a partir de los datos de la Base de Datos   
    def create_data_frame(self):
        #Conexion con la BD
        db = MySQLdb.connect(self.host, self.user, self.passw, self.dataBaseName)
        
        #Creamos el cursor de la base de datos
        cursor = db.cursor()
        
        #Realizamos la query buscando en el campo title
        cursor.execute("SELECT title FROM full_news_from_agencia_efe")
        
        #Creamos una lista de titles
        titles_list = self.run_query(cursor)
        
        #Creamos el dataframe a partir de la lista creada previamente    
        df = pd.DataFrame(titles_list)
        
        #Definimos el nombre de la columna
        df.columns = ['Title']
        
        return df
    
    
    #Funcion que ejecuta la query y retorna una lista con el resultado
    def run_query(self, cursor):
        title_list = []
        
        #Recorremos el resultado obtenido del query y agregamos cada titulo a la lista creada previamente
        for row in cursor.fetchall():
            title = row[0]
            title_list.append(title)
        
        return title_list