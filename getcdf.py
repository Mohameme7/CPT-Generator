import cdsapi

# Create an instance of the CDS API client
c = cdsapi.Client()

# Define the request parameters and retrieve the data
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': '2m_temperature',
        'year': '2024',
        'month': '07',
        'day': [
            '01', '02', '03'
        ],
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
        ],
        'area': [
            60, -10, 30, 40,
        ],
        'format': 'netcdf'
    },
    '2m_temperature_2024_07.nc'
)
