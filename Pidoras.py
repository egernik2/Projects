import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")


def new():
    logging.info('Module starting...')
    print('Some loading files and options')
    logging.info('Module started!')

if __name__ == '__main__':
    new()