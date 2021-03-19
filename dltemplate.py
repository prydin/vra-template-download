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
parser.add_argument('--insecure', help='Skip cert validation', action='store_true')

args = parser.parse_args()
verify=not args.insecure

payload = {
    "refreshToken": args.token
}
response = requests.post(args.url + "/iaas/api/login", json=payload, headers=headers, verify=verify)
headers["Authorization"] = "Bearer " + response.json()["token"]

if args.tid:
    tid = args.tid
else:
    response = requests.get(args.url + '/blueprint/api/blueprints?name=' + args.tname, headers=headers, verify=verify)
    tid = response.json()['content'][0]['id']

response = requests.get(args.url + '/blueprint/api/blueprints/' + tid, headers=headers, verify=verify)
print(response.json()['content'])