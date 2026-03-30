import requests
import json

base_url = "https://gorest.co.in"

AuthToken = "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad"


#Put Method
def update_user(id,name,email):
    url = f"{base_url}/public/v2/users/{id}"
    headers = {
        "Authorization" : "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad",
        }
    payload = {
        "name" : "Update_vatsal",
        "email" : "updatevatsal@gmai.com"
    }
    response = requests.put(url, headers=headers , json = payload)
    if response.status_code == 200:
        return "User updated successfully"
    else:
        raise Exception("Failed to create user")





#Main Function
def main():

    try :
        update_us = update_user(8406387, "updated", "updated@gmail.com")
        print(update_us)
    except:
        print("An error occurred while creating user")       

if __name__ == "__main__":
    main()        