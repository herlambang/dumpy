import psutil
from . import libs

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def stats(self, parameter_list):
    mem = psutil.virtual_memory()
    return_value = {
        'cpu_percent': psutil.cpu_percent(),
        'cpu_count': psutil.cpu_count(),
        'mem_total': libs.sizeof_fmt(mem.total),
        'mem_available': libs.sizeof_fmt(mem.available),
        'mem_used': libs.sizeof_fmt(mem.used),
        'mem_used_percent': mem.percent,
    }
    return return_value