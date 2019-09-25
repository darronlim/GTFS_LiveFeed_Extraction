# GTFS_LiveFeed_Extraction
GTFS livefeed extraction developed for TransLink feed 

Python 3 is required for the applications.

## GTFS_RT_FeedDownloader.py

Application extracts from the TransLink GTFS RealTime Feed and creates new raw data files for each pull.

The following three folders are created for storing the pulled data:

TU = "TripUpdate entity"

VP = "VehiclePosition entity"

SA = "ServiceAlert entity"

FT = "File Tracker"

New files will continuously be created as the programs recieves from the feed and will be placed in corresponding folders.


## Trip Update Processor

Reads through Trip Update file tracker documents and converts the corresponding trip update raw data files and converts them into a csv format

## Vehicle Position Processor

Reads through Vehicle Position file tracker documents and converts the corresponding trip update raw data files and converts them into a csv format
