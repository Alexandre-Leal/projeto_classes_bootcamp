
from datetime import datetime, timedelta

def check_data_correta (data):
    format = "%d/%m/%Y"

    if data.lower() == "hoje":
        hoje = (datetime.today()).date()
        return hoje
    
    elif data.lower() == "amanha":
        amanha = (datetime.today() + timedelta(days=1)).date()
        return amanha
    
    try:
        datetime.strptime(data, format)
        print("This is the correct date string format.")
        return data
    except ValueError:
        raise print("Data no formato errado. Digite no formato dd/mm/yyyy. 'Hoje' e 'Amanha' também é válido")
     
