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

