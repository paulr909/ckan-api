# CKAN API Calls

Authorization: API Token  

## Endpoints
/api/3/action/dataset_purge

/api/3/action/datastore_create

/api/3/action/datastore_delete

/api/3/action/datastore_upsert

/api/3/action/package_create

/api/3/action/package_delete

/api/3/action/package_list

/api/3/action/resource_create

/api/3/action/resource_update


### export_sql.py
Export data to CSV files from AWS

### csv_json.py
Convert CSV files to JSON

### Define absolute file paths for both staging and production servers
Staging: /home/ckan-api/sample-data-test/test-data.csv

Production: /

## Test DataStore API
curl -X GET "https://www.website.com/data-portal/api/3/action/datastore_search?resource_id=_table_metadata"
