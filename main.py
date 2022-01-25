import multiprocessing as mp
import traceback as tb
from aiohttp import web

from server.server import app
from logs.logger import logger
from db.db_worker import DBDevices
from worker import Worker

if __name__ == '__main__':
    try:
        server = mp.Process(target=web.run_app, args=(app, ), kwargs={'port': 8081})
        server.start()
        logger.info("Web server started")

        db_devices = DBDevices()
        for plc in db_devices.get_devices():
            worker = Worker(**plc)
            worker_process = mp.Process(target=worker.run)
            worker_process.start()





    except Exception as error:
        logger.error(f'main.py error {error}:\n\n {tb.format_exc()}\n')
