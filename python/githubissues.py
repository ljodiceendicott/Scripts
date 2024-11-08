import requests
import json

# Enter your GitHub credentials
username = "ljodiceendicott"
password = 

# Enter the repository details
owner = "ljodiceendicott"
repo = "CrowdWatch"

headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}
# Enter the issue details
issues = [
    {"title": "Issue Title 1", "body": "Issue Description 1"},
    {"title": "Issue Title 2", "body": "Issue Description 2"},
    {"title": "Issue Title 3", "body": "Issue Description 3"}
]

for issue in issues:
    # Make the API request to create the issue
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.post(url, auth=(username, password),headers=headers, json=issue)

    # Print the response from the API
    print(json.dumps(response.json(), indent=4))
