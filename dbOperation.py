import os
import sqlite3

class db_operation:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.pathToFile = 'history_weather.db'
        self.sql_create_table_city = '''CREATE TABLE IF NOT EXISTS city (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    );'''
        self.sql_create_table_data = '''CREATE TABLE IF NOT EXISTS data (
                                    id integer PRIMARY KEY,
                                    date_time text NOT NULL,
                                    time_zone text NOT NULL,
                                    temp integer NULLABLE,
                                    humidity integer NULLABLE,
                                    pressure integer NULLABLE,
                                    clouds integer NULLABLE,
                                    wind_velocity integer NULLABLE,
                                    wind_direction integer NULLABLE,
                                    description text NULLABLE,
                                    FOREIGN KEY (id) REFERENCES city (id)
                                );'''
        self.sql_city_insert_with_param = '''INSERT INTO city
                                        (name) 
                                        VALUES (?);
                                    '''
        self.sql_data_insert_with_param = '''INSERT INTO data
                                        (date_time, time_zone, temp, humidity, pressure, clouds, wind_velocity,
                                        wind_direction, description)
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                                    '''
        self.sql_data_select = '''SELECT DISTINCT name FROM city'''

    def db_connect(self):
        try:
            self.connection = sqlite3.connect('history_weather.db')
            return self.connection
        except Exception as e:
            return False

    def db_create_tables(self):
        try:
            self.cursor = self.connection.cursor()
            self.connection.execute(self.sql_create_table_city)
            self.connection.execute(self.sql_create_table_data)
            return True
        except Exception as e:
            print(e)
            return False

    def db_insert(self, valData, valCity, valtimeZone, valTemp, valHumidity, valPressure, valClouds, valWindVel, valWindDir, valDescr):
        city_name = [valCity]
        dataParam = [valData, valtimeZone, valTemp, valHumidity, valPressure, valClouds, valWindVel, valWindDir, valDescr]
        try:
            self.connection.execute(self.sql_city_insert_with_param, city_name)
            self.connection.execute(self.sql_data_insert_with_param, dataParam)                   
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(e)
            return False
    def db_select(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.sql_data_select)
        self.records = self.cursor.fetchall()
        return self.records
        


#Use standalone
#if __name__ == "__main__":
#    my = db_operation()
#    connSuccess = my.db_connect()
#    if connSuccess:
#        create = my.db_create_tables()
#        if create:
#            insert = my.db_insert('2020-05-29 23:59:59', 'Jopinsk', 'Europe/Zadnitza', '35', '90', '778', '10', '4', '170', 'Очень жарко')
#            if insert:
#                print('Success')
#    else:
#        print('No execute')
#    my.db_select()



   

    