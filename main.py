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
# 4. Core sends a new dictionary to the Presenter
# 5. Presenter builds a new page - then sends to View


#################
#### IMPORTS ####
import datetime
import random


######################
#### HAUGHTY CORE ####
class core:

    def storeNewBofr(title, body):
        date = datetime.datetime.now()
        date_format = date.strftime("%Y%m%d")
        return {"title": title, "body": body, "stamp": date_format,}


###################
#### PRESENTER ####
class presenter:

    def newTicket(json_data):
        f = open("lib/UIDs.csv")
        UIDs = f.read()
        UID = str(random.randrange(10, 99, 1))
        while UID in UIDs:
            UID = str(random.randrange(10, 99, 1))
        json_data["UID"] = UID
        f.close()
        f = open("lib/UIDs.csv", "a")
        f.write(UID + ",")
        f.close()
        return json_data
