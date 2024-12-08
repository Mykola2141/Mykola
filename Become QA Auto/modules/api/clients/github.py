import requests


class GitHub:
    
    def get_user(self, username):
        r=requests.get(f'https://api.github.com/users/{username}')
        body=r.json()

        return body
    def search_repo(self, name):
        r=requests.get (
            "https://api.github.com/search/repositories",
            params={"q":name}
        )
        body=r.json()

        return body
    
    def get_commit(self,commit):
        r=requests.get(f'https://api.github.com/search/commits?q={commit}')
        body=r.json()

        return body