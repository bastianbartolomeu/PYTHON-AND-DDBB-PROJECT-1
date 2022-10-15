import mysql.connector 

class dbuc :
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='batman2022',
            db='infoaeropuertos'
        )
        self.cursor = self.mydb.cursor()
        print(self.mydb)
        print('----------------------------------------------- ')
        print('                CONEXION EXITOSA' )
        print('----------------------------------------------- ')
        
    def mostrar_aeropuertos(self):
        sql ='SELECT * FROM aeropuertos'
        try:
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            contador =1 
            for lista in listados:
                print(contador, '| ', lista)
                contador +=1
        except Exception as e:
            raise
    
    def insertar_registro(self):
        try:
            self.cursor = self.mydb.cursor()
            sql = '''INSERT INTO infoaeropuertos.aeropuertos (id,ident,type,name,elevation_ft,municipality,iata_code,score)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
            filas = [
            (39340,'SHCC','heliport','Clinica Las Condes Heliport',2461,'Santiago',' ',25),
            (39379,'SHMA','heliport','Clinica Santa Maria Heliport',2028,'Santiago',' ',25 ),
            (39390,'SHPT','heliport','Portillo Heliport',9000,'Santiago', ' ',25)  
                  ]
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('        REGISTROS INSERTADOS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
    
    def new_datos(self):
        sql ='SELECT * FROM infoaeropuertos.aeropuertos WHERE id IN (39340,39379,39390)'
        try:
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            contador = 1 
            print('-------------------------------------------------------------')
            print('           NUEVOS DATOS INSERTADOS SON LOS SIGUENTE :  ')
            for lista in listados:
                print("--------------------------------------------------------------------------------------------")
                print(contador,'|', lista, '|')
                contador +=1
            print("--------------------------------------------------------------------------------------------")
        except Exception as e:
            raise
    
    def aeropuerto_altura(self):
        sql =''' SELECT * FROM infoaeropuertos.aeropuertos 
                WHERE elevation_ft > 5000 
                ORDER BY elevation_ft DESC '''
        try:
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            contador =1 
            for lista in listados:
                print("--------------------------------------------------------------------------------------------")
                print(contador, '|', lista,'|')
                contador +=1
            print("--------------------------------------------------------------------------------------------")
            print('''  
            EXISTE UN TOTAL DE : ''', contador - 1, ''' AEROPUERTOS SITUADOS A MÁS DE 5000 pies DE ALTURA
                  ''')
        except Exception as e:
            raise
        
    def detalles_aeropuerto(self):
        sql =''' SELECT name,type,municipality,elevation_ft FROM infoaeropuertos.aeropuertos
        WHERE elevation_ft > 5000 ORDER BY elevation_ft DESC'''   
        try:
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            contador =1 
            for lista in listados:
                print("--------------------------------------------------------------------------------------------")
                print(contador, '|', 'Nombre :',lista[0],'|','tipo :',lista[1],'|','Municipalidad :',lista[2],'|','Altura : ',lista[3],'|')
                contador +=1
            print("--------------------------------------------------------------------------------------------")
            print('''  
            EXISTE UN TOTAL DE : ''', contador -1 , ''' AEROPUERTOS SITUADOS A MÁS DE 5000 pies DE ALTURA
                  ''')
        except Exception as e:
            raise



database = dbuc()
#database.insertar_registro()
#database.mostrar_aeropuertos()
#database.new_datos()
database.aeropuerto_altura()
#database.detalles_aeropuerto()
