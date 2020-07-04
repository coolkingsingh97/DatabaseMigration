import os

DB_DETAILS = {
    'dev':{
        'SOURCE_DB': {
            'DB_TYPE':'mysql',
            'DB_HOST':'<ENTER HOST IP>',
            'DB_NAME':'RETAIL_DB',
            'DB_USER':os.environ.get('DB_USER'),
            'DB_PASS':os.environ.get('DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE':'postgres',
            'DB_HOST':'<ENTER HOST IP>',
            'DB_NAME':'RETAIL_DB',
            'DB_USER':'RETAIL_USER',
            'DB_PASS':'KULRAJ'
        }
    }
}