import requests


class GetDoggo:

    @staticmethod
    def get_doggo(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("successfully fetched the data")
            print(response.text)
            doggo = response.text
            return doggo
        return "Could not get doggo picture"
