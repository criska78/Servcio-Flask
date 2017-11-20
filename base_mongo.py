from pymongo import MongoClient
from datetime import datetime
from config import *
"""funcion que me guarda los logs de flask en mongo"""
def base_mongo(valor_fecha,valor_entero,valor_text,valor_ente,valor_tex,valor_textou):
	log={
        'fecha_invocacion': valor_fecha,
        'estado': {
            'codigo': valor_entero,
            'texto': valor_text
        },
        'respuesta': {
            'largo': valor_ente,
            'tipo': valor_tex
        },
        'usuario': valor_textou,
        #'direccion_consulta': [valor_ip, valor_puerto]
    }

	
	client=MongoClient(credencial_mongo)
	db=client['proyecto']
	collection=db['logs']
	collection.insert_one(log)
	




	


