# LET'S START with the basics
# 
# At a high level, the 0.1 version must be able to:
# 1. Let users submit a bug or feature request
# 
bofr_properties = {
        "Status": "New",
        "Title": "",
        "Project": "",
        "Content": "",
}

def submit_bofr(new_bofr):
    # 1.2 Specify - bug or feature request?
    bofr = str(input("Bug or feature request? "))

    # 1.3 Ask the user to provide a title (max 140 characters)
    new_title = str(input("New " + bofr + "\nTitle (max 140 characters): "))
    if len(new_title) > 140:
        new_title = new_title[:140]
        print("Title exceeds 140 characters - saved as:\n" + new_title)

    # 1.4 Ask the user to assign a project
    new_project = str(input("Which project does this apply to? "))

    # 1.5 Ask user to provide details
    new_content = str(input("Please provide all relevant details (up to 1000 characters).\n"))
    if len(new_content) > 1000:
        new_content = new_content[:1000]
        print("Content exceeds 1000 characters - saved as:\n" + new_content)

    # 1.6 Store details in dict
    new_bofr["Title"] = new_title
    new_bofr["Project"] = new_project
    new_bofr["Content"] = new_content

    for k,v in bofr_properties.items():
        print(k, v)

    return new_bofr


submit_bofr(bofr_properties)
