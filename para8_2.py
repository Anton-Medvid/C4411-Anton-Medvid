import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='para8_2_logs.log',
                    filemode='w',
                    format='WE have a message:%(asctime)s:@:%(levelname)s - %(message)s')
try:
    print(10/0)
except Exception:
    logging.exception('Exception')
