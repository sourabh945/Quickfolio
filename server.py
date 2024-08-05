from app import app

import multiprocessing

from gunicorn.app.base import BaseApplication



class HttpSErver(BaseApplication):

    def __init__(self, app:Flask ,option=None, usage=None, prog=None):
        self.application = app
        self.option = option or {}
        super().__init__(usage, prog)


    def load_config(self):
        for key , value in self.option.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(),value)

    def load(self):
        return self.application




if __name__ == "__main__":

    nums_workers = multiprocessing.cpu_count()*2+1

    option = {
        'bind':'0.0.0.0:5000',
        'workers': nums_workers,
        'worker_class' : 'gevent',
        'worker_connection' : 1000,

        'timeout':30,
        'graceful_timeout':30,
        'keepalive':2,

        'errorlog':"-",
        'accesslog':"-",
        'loglevel':'info',

        'preload_app':True,

        'keyfile':'./certificates/key.pem',
        'certfile':'./certificates/cert.pem'
    }

    HttpSErver(app,option).run()
