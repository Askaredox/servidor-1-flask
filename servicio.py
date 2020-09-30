import requests


class Servicio:
    URL1 = 'http://172.19.0.2:5000/api'
    URL2 = 'http://172.19.0.3:5000/api'

    @staticmethod
    def send_data(autor, nota):
        data = Servicio.objectify(autor, nota)
        res = {}
        cp1 = requests.get(Servicio.URL1+"/status")
        cp2 = requests.get(Servicio.URL2+"/status")
        if cp1.status_code != 200 and cp2.status_code != 200:
            return {'id':-1}
        
        if cp1.status_code == 200 and cp2.status_code != 200:
            res = requests.post(Servicio.URL1, json=data)
        elif cp2.status_code == 200 and cp1.status_code != 200:
            res = requests.post(Servicio.URL2, json=data)
        else:
            if cp2['len'] < cp1['len']:
                res = requests.post(Servicio.URL2, json=data)
            elif cp1['len'] < cp2['len']:
                res = requests.post(Servicio.URL1, json=data)
            else:
                if cp2['ram'] < cp1['ram']:
                    res = requests.post(Servicio.URL2, json=data)
                elif cp1['ram'] < cp2['ram']:
                    res = requests.post(Servicio.URL1, json=data)
                else:
                    if cp2['cpu'] <= cp1['cpu']:
                        res = requests.post(Servicio.URL2, json=data)
                    else:
                        res = requests.post(Servicio.URL1, json=data)
        body = res.json()
        return body

    @staticmethod
    def objectify(autor, nota):
        return {
            'autor': autor,
            'nota':nota
        }