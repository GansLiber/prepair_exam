from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

slaves_dict = {
    'rauf': 'Рауф парень работящий',
    'leon': 'Да, это негр Леон, умеет мыть посуду',
    'gabba': 'Габба гребет славно!',
    'buf': 'Негр Буф крутой ловец рыб',
    'buf': 'Негр Буф крутой ловец рыб',
}


def get_type_slave(request, type_slave: str):
    description = slaves_dict.get(type_slave, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{type_slave} - такого раба нет, но возможно появиться позже")

def get_number(request, type_slave: int):
    slaves = list(slaves_dict)
    if type_slave > len(slaves):
        return HttpResponseNotFound(f'у нас не так много рабов, у нас меньше - {type_slave}')
    name_slave = slaves[type_slave-1]
    return HttpResponseRedirect(f'/slaves/{name_slave}')