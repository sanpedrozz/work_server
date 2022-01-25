import multiprocessing as mp
import traceback as tb

from aiohttp import web

from server.server import app
from logs.logger import logger
from db.db_worker import DBDevices


# from worker import Worker
from config import Config

if __name__ == '__main__':
    try:
        server = mp.Process(target=web.run_app, args=(app, ), kwargs={'port': 8081})
        server.start()
        logger.info("Web server started")

        db_worker = DBDevices()
        for plc in db_worker.get_devices():
            worker = Worker(**plc)
            worker_process = mp.Process(target=worker.run)
            worker_process.start()

        # # db_worker.run()
        # db_worker_process = mp.Process(target=db_worker.run)
        # db_worker_process.start()



    except Exception as error:
        logger.error(f'main.py error {error}:\n\n {tb.format_exc()}\n')
