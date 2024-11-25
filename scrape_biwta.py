#!/usr/bin/env python

import pandas as pd
import geopandas as gpd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def update_sensors(url='http://biwta.port-log.net/live/map/3.0/src/data/plg/sensors.geojson'):
    gdf_sensors = gpd.read_file(url)
    gdf_sensors = gdf_sensors.set_index('id')

    stn_updated = 0
    stn_total = 0

    for idx, sensor in gdf_sensors.iterrows():
        stn_total += 1
        site_name = sensor.site_name.replace(' ', '').replace('.', '')
        site_id = sensor.idsite
        sensor_id = idx.split(':')[1]
        
        datasets = sensor.datasets
        for dsname in datasets:
            parameters = datasets[dsname]['parameters']
            for paramname in parameters:
                paramvalues = parameters[paramname]
                fname = outdir / f'{site_id}.{site_name}.{sensor_id}.{dsname}.{paramname}.csv'
                if fname.exists():
                    _df = pd.read_csv(fname, parse_dates=True, index_col='Datetime')
                else:
                    _df = pd.DataFrame()
                
                datetime = pd.to_datetime(paramvalues['datetime']*1e9)
                if datetime in _df.index:
                    pass
                else:
                    record = pd.DataFrame({
                        'Datetime':[datetime],
                        paramname:[paramvalues['value']]
                    }).set_index('Datetime')
                    _df = pd.concat([_df, record])
                    _df.to_csv(fname, index_label='Datetime')
                    stn_updated += 1

    logger.info(f'{stn_updated}/{stn_total}')

    df_sensors = gdf_sensors.loc[:, ['idsite','latitude', 'longitude', 'site_name', 'description', 'owner', 'time_zone', 'active', 'status']]
    df_sensors.to_csv('sensors.csv')

if __name__=='__main__':
    logging.basicConfig(
        filename='scrape.log', 
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s")
    
    outdir = Path('./records')
    if not outdir.exists():
        outdir.mkdir(parents=True)
    
    update_sensors()
