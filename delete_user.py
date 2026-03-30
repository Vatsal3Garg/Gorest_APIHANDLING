import requests
import json

base_url = "https://gorest.co.in"

AuthToken = "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad"

#Delete Method
def dlt_users(id):
    url = f"{base_url}/public/v2/users/{id}"
    headers = {"Authorization": AuthToken}
    response = requests.delete(url, headers=headers)
    
    
    if response.status_code == 204 :
       
        return "User data Deleted"
    else:
        raise Exception("Failed to fetch user data")       



#Main Function
def main():
    try :
        users_delete = dlt_users(8406604)
        print(users_delete)
    except:
        print("An error occurred while DELETING") 



if __name__ == "__main__":
    main()        