###################
#### STRUCTURE ####
# 
# Haughty core:
#   business logic
# 
# Entity: database:
#   stores and retrieves tickets
# 
# Presenter:
#   Prepares data for output by the view
# 
# STORY I: user writes & saves new ticket
# 1. User types entries into Title, Body, and Affected System fields - then hits Save
# 2. Presenter retrieves the data, validates it - then sends to Core
# 3. Core logic stores data in Database
# 4. 


#################
#### IMPORTS ####
import datetime


######################
#### HAUGHTY CORE ####
class core:

    def storeNewBofr(title, body):
        date = datetime.datetime.now()
        date_format = date.strftime("%Y%m%d")
        return {"title": title, "body": body, "stamp": date_format,}


# def main():

