import requests
import json

base_url = "https://gorest.co.in"

AuthToken = "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad"




#Post Method
def create_user(name, email, gender):
    url = f"{base_url}/public/v2/users"
    headers = {
        "Authorization" : "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad",
        }
    payload = {
        "name": name,
        "email": email,
        "gender": gender,
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return "User created successfully"
    else:
        raise Exception("Failed to create user")



#Main Function
def main():
 
    try :
        create_us = create_user("bharat", "bharatgarg@gmail.com", "male")
        print(create_us)
    except:
        print("An error occurred while creating user")    



if __name__ == "__main__":
    main()        