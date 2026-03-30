import requests
import json

base_url = "https://gorest.co.in"

AuthToken = "Bearer 81d9327f601fd012e534f6e6e506ac54ef4ab46a8e7498c2ca1fb4ac5b1415ad"

#Get Method
def get_users():
    url = f"{base_url}/public/v2/users"
    headers = {"Authorization": AuthToken}
    response = requests.get(url, headers=headers)
    all_user_data = response.json()
    json_str = json.dumps(all_user_data, indent=4)
    if response.status_code == 200 and all_user_data != []:
        print("User data fetching.........wait a moment")
        return json_str
    else:
        raise Exception("Failed to fetch user data")       



#Main Function
def main():
    try :
        users_data_list = get_users()
        print(users_data_list)
    except:
        print("An error occurred while fetching user data") 



if __name__ == "__main__":
    main()        