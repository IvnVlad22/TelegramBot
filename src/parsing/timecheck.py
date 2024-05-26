import datetime

def tmchk(message) -> bool:
    ## Берем настоящее время
    current_time = datetime.datetime.now()
    ## берем время пришедшего сообщения
    message_time = datetime.datetime.fromtimestamp(message.date)
    ## Находим разницу
    time_difference = current_time - message_time
    ## Сравниваем
    return time_difference.total_seconds() < 20 * 60