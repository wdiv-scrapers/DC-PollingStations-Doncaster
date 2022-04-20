from dc_base_scrapers.arcgis_scraper import UnsortedArcGisScraper

root_url = "https://gis.doncaster.gov.uk/arcgis/rest/services/ElectionSearch/FeatureServer"
stations_url = "{root_url}/0/query?where=OBJECTID+LIKE+'%25'&outFields=OBJECTID%2CPOLLINGPLA%2CUPRN%2CADDRESS%2CWARD%2CPOLLING_DI&geometryType=esriGeometryPoint&spatialRel=esriSpatialRelIntersects&units=esriSRUnit_Meter&returnGeometry=true&outSR=4326&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnZ=false&returnM=false&f=pjson".format(root_url=root_url)
districts_url = "{root_url}/0/query?where=OBJECTID+LIKE+'%25'&outFields=OBJECTID%2CCODE&geometryType=esriGeometryPoint&spatialRel=esriSpatialRelIntersects&units=esriSRUnit_Meter&returnGeometry=true&outSR=4326&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnZ=false&returnM=false&f=pjson".format(root_url=root_url)
council_id = 'DNC'


stations_scraper = UnsortedArcGisScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = UnsortedArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
