from __future__ import print_function
import httplib2
import os
import csv

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from config import *
"""CONEXION A PLANILLA DE GOOGLE SHEETS"""
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
"""AQUI VAN LAS CREDENCIALES : SCOPES,CLIENT_SECRET_FILE Y APPLICATION_NAME,
LAS CUAL IMPORTO DEL ARCHIVO DE CONFIGURACION"""

def get_credentials():
    """FUNCION PARA VALIDAR LAS CREDENCIALES"""
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """FUNCION QUE ME GUARDA LA PLANILLA DE GOOGLE SHEETS EN LA CARPETA TEMPLATES
    PARA PODER UTILIZARLA EN FLASK"""
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1EbULy_YSQ5UHDUo2Tz5lrUtmeCpm8Y1pNlFao0tqVyQ'
    rangeName = 'Form Responses 1!A1:U'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values')
    with open('C:\\Users\\Ceibal\\Desktop\\pro\\templates\\Microdatos.csv', 'w') as fichero:
        writer = csv.writer(fichero)
        writer.writerows(values)
            
if __name__ == '__main__':
    main()
