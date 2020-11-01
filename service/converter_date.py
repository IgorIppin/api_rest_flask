# Logica del conversor de fechas y del formato de respuesta

from datetime import datetime


def converter(original_date):
    # Preparar el string con la fecha para datetime
    try:
        date = original_date.split("-")
        date = tuple(map(int, date))

        # Crear fecha formato datetime
        new_date = datetime(date[0], date[1], date[2])

        # Cambiar el formato a timestamp
        timestamp_date = int(datetime.timestamp(new_date))

        return create_json(original_date, timestamp_date)
    except ValueError:
        return {"error": "El formato o la fecha es incorrecto."}


def create_json(original_date, timestamp_date):
    # Montar los datos que devuelve la api
    return {
        "original_date": original_date,
        "timestamp": timestamp_date
    }
