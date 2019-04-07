# Import population raster and convert to polygons

import rasterio
from rasterio.mask import mask
import geopandas as gpd
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

# applied example: http://www.guilles.website/2018/06/12/tutorial-exploring-raster-and-vector-geographic-data-with-rasterio-and-geopandas/

# I have not found a way to get a raster from in memory data. So I have loaded it from the file written above.
gtroads_osm_raster = rasterio.open("GtRoads_OSM_100m_x_100m.tif", 'r')
gtroads_osm_r = gtroads_osm_raster.read()

gtroads_osm_filtered = ndi.maximum_filter(gtroads_osm_r, size= 5 )

gtroads_access_osm = wpgt[0] * gtroads_osm_filtered[0]

plt.rcParams['figure.figsize'] = 14, 14
plt.imshow(np.log10((np.fmax( gtroads_access_osm+1, 1))), vmin = 0, interpolation="bilinear")
bar = plt.colorbar(fraction=0.03)
bar.set_ticks([0, 0.301, 1.041, 1.708, 2.0043])
bar.set_ticklabels([0, 1, 10, 50, 100])

# Now let's get Guatemala municipalities shapes
gpmunis_json = fiona.open("../../../DATOS/IGN/GT-IGN-cartografia_basica-Division politica Administrativa (Municipios).geojson", "r", "GeoJSON")
gpmunis = geopandas.GeoDataFrame.from_features(gpmunis_json)

munis_pop = []
for muni in gpmunis_json:
    subr, bounds = mask.mask(wpgt_r, [muni["geometry"]])
    munis_pop.append({
        "road_access": np.sum(gtroads_access_osm[subr.data[0]>0]),
        "total_pop": np.sum(subr.data[subr.data>0]),
        "codigo": muni["properties"]["COD_MUNI__"]
    }) 
    print("processes muni ", muni["properties"]["COD_MUNI__"])
                                                                     

pop_vector = gpd.GeoDataFrame.from_postgis('''SELECT * FROM {table}'''.format(id = 'Adm3Name',table = areas[0]['name_s']), engine, geom_col='geom' )   

with rasterio.open(population_raster['data']) as src:
    # set pop_vector to match crs of input raster
    # the above works as tested (raster is epsg 4326)
    # in theory, works if epsg is otherwise detectable in rasterio
    pop_vector.to_crs({'init':test.crs['init']},inplace=True)
    geoms = pop_vector.to_json)
    
     out_image, out_transform = mask(src, geoms, crop=True)
                                                                   
gdf.to_crs(epsg=4326, inplace=True) 


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
