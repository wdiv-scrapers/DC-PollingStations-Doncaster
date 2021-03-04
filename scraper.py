from dc_base_scrapers.arcgis_scraper import ArcGisScraper


stations_url = "https://gis.doncaster.gov.uk/arcgis/rest/services/ElectionSearch/FeatureServer/0/query?where=OBJECTID+LIKE+%27%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&gdbVersion=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=&resultOffset=&resultRecordCount=&f=pjson"
districts_url = "https://gis.doncaster.gov.uk/arcgis/rest/services/ElectionSearch/FeatureServer/1/query?where=OBJECTID+LIKE+%27%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&gdbVersion=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=&resultOffset=&resultRecordCount=&f=pjson"
council_id = 'DNC'


stations_scraper = ArcGisScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
