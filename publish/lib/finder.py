def insertBlogInTemplate():
    template = open("template.html", "r+")
    l = ""
    while l != "abcblogtimexyz":
        pos = template.tell()
        l = template.readline()
    template.seek(pos)
    template.write("Check this out!")

insertBlogInTemplate()

#        l = template.readline()
#    while l == "y":

