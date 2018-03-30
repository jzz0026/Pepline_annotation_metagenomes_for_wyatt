import pandas as pd
## sort hmm result and get the top hit for each read (sorted by Score)

from sys import argv

script, file_name = argv



df = pd.read_csv(file_name,sep="\t",header=None)
df = df[0].str.split(" +",expand=True)
df1 = df.iloc[:-10,[0,2,3,4,5]]
df1.columns = ["Query_orfs","KO ID","HMM ID","E-value","Score"]
df1["Query"] = df1["Query_orfs"].str.split("_",expand=True)[0] 
df2 = df1.sort_values(["Query","Score"],ascending=False)
df3 = df2.groupby("Query",as_index=False).first() ## get the best hit for each read!! not orf!!
df3.to_csv(file_name.split(".")[0] +"_filtered_hmm.result")



df3["KO ID"] = df3["KO ID"].str.replace("KO:","").str.replace("_.*","")
df4 = df3[["KO ID","HMM ID"]]


df5 = pd.DataFrame(df4["KO ID"].str.split(',').tolist(), index=df4["HMM ID"]).stack() ##transform hmmID count to KO counts
df5 = df5.reset_index()[[0, "HMM ID"]]
df5.columns = ["KO ID","HMM ID"]

df6 = pd.DataFrame(df5.groupby("KO ID").size())
df6.columns = ["Counts"]
df6.to_csv(file_name.split(".")[0] +"_filtered_hmm.summary")