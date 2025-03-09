import pandas as pd
df=pd.read_csv("data/issues/issues.csv")
df1=pd.DataFrame()
df1["Answer"]=df["issuetype"]
df1["Question"] = "Can you give me details about the issue?"
df1.to_csv("data/issues/issues_process.csv",index=False)