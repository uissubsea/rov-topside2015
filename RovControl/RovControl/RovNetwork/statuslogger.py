import sys
sys.path.insert(1, '../Controller')

import logging


logger = logging.getLogger("clientlog")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(module)s][%(funcName)s] %(message)s'
logging.basicConfig(format=FORMAT)

