# Import population raster and convert to polygons

import time
import raster2pgsql
from sqlalchemy import create_engine
from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start  = time.time()
script = os.path.basename(sys.argv[0])

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))
# import population raster

# https://postgis.net/docs/RT_ST_PixelAsPolygons.html

# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
