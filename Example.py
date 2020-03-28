#!/usr/bin/env python3

import os
import sys

# look for libraries that are configured by './build.sh'
cwd = os.getcwd()

# Add `/lib` to the path to pick up our pip installed 3rd party requirements
sys.path[0:0] = ["{}/lib".format(cwd)]

# Add '/huvr_api_client' to the path to make this runnable out of the source tree
sys.path[0:0] = ["{}/covid_19_data_parser".format(cwd)]

from covid_19_data_parser import Client, Parser




# time_series_covid19_confirmed_global_csv_url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
time_series_covid19_confirmed_global_csv_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
filename = 'downloads/confirmed_global_data.csv'

parser = Parser(confirmed_data_file=filename)
if not parser.cached_csv():
    print("Fetching csv file from {}".format(time_series_covid19_confirmed_global))
    client = Client()
    ( res_code, data ) = client.get(time_series_covid19_confirmed_global_csv_url)
    if res_code == 200:
        print("Successfully Downloaded data {}".format(len(data)))
        res = parser.write_csv_file(filename, data)
        if res:
            print("Successfully Wrote datafile {}".format(filename))

print("Parsing CSV data")
parser.parse_time_series('US')