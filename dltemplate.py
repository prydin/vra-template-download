import requests
import argparse

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

parser = argparse.ArgumentParser(description='NSXcheck');
parser.add_argument('--url', help='The vRA URL')
parser.add_argument('--token', type=str, help='The vRA API token')
parser.add_argument('--tname', help='The template name')
parser.add_argument('--tid', help='The template ID')
args = parser.parse_args()

payload = {
    "refreshToken": args.token
}
response = requests.post(args.url + "/iaas/api/login", json=payload, headers=headers)
headers["Authorization"] = "Bearer " + response.json()["token"]

if args.tid:
    tid = args.tid
else:
    response = requests.get(args.url + '/blueprint/api/blueprints?name=' + args.tname, headers=headers)
    tid = response.json()['content'][0]['id']

response = requests.get(args.url + '/blueprint/api/blueprints/' + tid, headers=headers)
print(response.json()['content'])