import requests

class Github:
     def __init__(self):
          self.api_url = "https://api.github.com"
          self.token = "41d55c2de3687049c5af7d5946f4a699e8cb2ebe"

     def getUser(self, username):
          response = requests.get(self.api_url+ "/users/" + username)
          return response.json()

     def getRepositories(self,username):
          response = requests.get(self.api_url+ "/users/" + username + "/repos")
          return response.json()

     def createRepository(self,name):
          response = requests.post(self.api_url + "/user/repos?access_token=" + self.token, json= {
               "name": name,
               "description": "This is your first repository",
               "homepage": "https://github.com",
               "private": False,
               "has_issues": True,
               "has_projects": True,
               "has_wiki": True
          })
          return response.json()


test = Github()


while True:
     secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçiminiz: ")

     if secim == "4":
          break
     elif secim == "1":
          username = input("Username: ")
          result = test.getUser(username)
          print(f'name: {result["name"]} repositories: {result["public_repos"]} followers: {result["followers"]}')
     elif secim == "2":
          username = input("Username: ")
          result = test.getRepositories(username)
          for repo in result:
               print(f'Repo ID: {repo["id"]} Repo Name: {repo["name"]}\nRepo Description: {repo["description"]}')
     elif secim == "3":
          name = input("Repository Name: ")
          result = test.createRepository(name)
          print(result)
     else:
          print("Hatalı bilgi girdiniz.")

