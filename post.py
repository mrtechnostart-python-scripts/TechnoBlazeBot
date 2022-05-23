import requests
base_url = "https://api.telegram.org/bot{BOTAPIHERE}/" # Used To Control Bot Via Telegram Bot API
def device_check(offset): # Check If Device Is Official & Updates Message ID
    parameters = {
        "offset" : offset
    }
    official_devices = ["surya","onclite","sweet","davinci","santoni"] # Add Your Official Devices Here
    resp = requests.get(base_url+"getUpdates", data = parameters) # getUpdates fetches updates from URL
    data = resp.json() # Converts resp to json
    for i in data["result"]: # Basic Loops To Iterate And Check For Official Devices
        for j in official_devices:
            try:
                if i["message"]["text"] == "/release "+j:
                    sendPost(i["message"]["text"][9::]) # Returns Only codeName and slice '/release'
            except KeyError: # Prevent Sudden Crash Of Program Due To Key Error In Case Of No 'text' Field
                continue
    if data["result"]: # Updates Offset
        return data["result"][-1]["update_id"] + 1
offset = 0
while True:
    offset = device_check(offset) 
