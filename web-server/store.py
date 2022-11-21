import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)            #Estado HTTP: Código de 3 dígitos que indica el estado de la solicitud
    print(r.text)                   #Nos retorna el texto de nuestra solicitud
    print(type(r.text))             #Queremos ver de qué tipo es el texto/variable solicitado
    categories = r.json()           #type(r.text) es un string, esta info, aunque tiene la estructura de un
                                    #diccionario, no es interpretable/operable por ser tipo string,
                                    #y con r.json() obtenemos la información en un formato json
                                    # tipo lista operable desde nuestro código Python
    for category in categories:
        print(category['name'])     #Con nuestra variable categories en formato json, podemos acceder
                                    #a la información dentro de nuestra variable