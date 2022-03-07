import os
import csv
import json
import urllib.request
import pydig

csvUrl = 'https://raw.githubusercontent.com/cisagov/dotgov-data/main/current-federal.csv'
commitsUrl = 'https://api.github.com/repos/cisagov/dotgov-data/commits?path=current-federal.csv&page=1&per_page=1'

# Compare dates of local file and last commit date of remote file
# localDateStamp = os.path.getmtime('data/current-federal.csv')
# print(localDateStamp)

# commitsData = urllib.request.urlopen(commitsUrl).read()
# commitsJson = json.loads(commitsData)
# latestCommitDate = commitsJson[0]['commit']['committer']['date']
# print(latestCommitDate)

# If there are no changes then commit won't be available
csvData, headers = urllib.request.urlretrieve(csvUrl, filename="data/current-federal.csv")
urllib.request.urlcleanup()

resolver = pydig.Resolver(
    additional_args=[
        '+time=10',
    ]
)

with open('data/current-federal.csv', 'r') as file:
    data = csv.DictReader(file)
    for row in data:
        name = row['Domain Name']
        print(name)
        ns = resolver.query(name, 'NS')
        print(ns)