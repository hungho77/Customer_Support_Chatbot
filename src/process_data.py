import json 
import csv
json_path=('/home/lybui/Desktop/Work/Customer_Support_Chatbot/data/vcb/jira_data_1741318923069.json')

with open(json_path, 'r') as j:
    contents = json.loads(j.read())

key_important = [
    "issuetype", "description", "project", "watches", "created",
    "priority", "assignee", "updated", "status", "summary", "creator",
    "subtasks", "reporter", "aggregateprogress", "progress", "votes"
]
data = []
for issue in contents["issues"]:
    row = {key: issue["fields"].get(key, "") for key in key_important}
    data.append(row)
    
csv_filename = "issues.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=key_important)
    writer.writeheader()
    writer.writerows(data)
