# Import population raster and convert to polygons

import time
from osgeo import gdal, ogr
import sys
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

# this allows GDAL to throw Python Exceptions
gdal.UseExceptions()

src_ds = gdal.Open(population_raster[0])
if src_ds is None:
    print('Unable to open {}'.format(src_filename))
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(population_raster[1])
except RuntimeError as e:
    # for example, try GetRasterBand(10)
    print('Band ( {} ) not found'.format(population_raster[1]))
    print(e)
    sys.exit(1)

#
#  create output datasource
#
dst_layername = population_grid
drv = ogr.GetDriverByName("ESRI Shapefile")
dst_ds = drv.CreateDataSource( dst_layername + ".shp" )
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )

gdal.Polygonize( srcband, None, dst_layer, -1, [], callback=None )


# https://postgis.net/docs/RT_ST_PixelAsPolygons.html

# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
