
########################################
# My custom logger
########################################

from datetime import datetime # log file name
from os.path import join
from pathlib import Path    # to create directory

import logging
import os

def main():
    log_folder_path = os.path.dirname(os.path.abspath(__file__))
    Path(str(__file__).replace('.py', '_log')).mkdir(parents=True, exist_ok=True) 
    log_folder_path = join(log_folder_path, str(__file__).replace('.py', '_log'))
    log_file_name = datetime.now().strftime('run_%Y_%m_%d_%H_%M.log')
    log_file_path = join(log_folder_path, log_file_name)
    logging.basicConfig(filename=log_file_path, level=logging.DEBUG, 
                        format='%(asctime)s %(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S%p    ')
    logging.info('-'*25)
    logging.info('My Logger: ')
    logging.info('-'*25)
    logging.info('Program folder: {}'.format(log_folder_path))
    
if __name__ == "__main__":
    main()
