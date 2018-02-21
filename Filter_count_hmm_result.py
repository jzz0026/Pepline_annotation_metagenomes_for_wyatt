
# coding: utf-8

# In[3]:


import pandas as pd
from sys import argv

script, file_name = argv
#file_name = "Browns_ThreeSqA_D1_extractCH4.tab"


# In[3]:


df = pd.read_csv(file_name,sep="\t",header=None)
df = df[0].str.split(" +",expand=True)
df1 = df.iloc[:-10,[0,2,3,4]]
df1.columns = ["Query_orfs","KO ID","HMM ID","E-value"]
df1["Query"] = df1["Query_orfs"].str.split("_",expand=True)[0] 
df2 = df1.sort_values(["Query","E-value"])
df3 = df2.groupby("Query",as_index=False).first() ## get the best hit for each read!! not orf!!
df3.to_csv(file_name.split(".")[0] +"_filtered_hmm.result")


# In[6]:


#df3 = pd.read_csv(file_name.split(".")[0] +"_filtered_hmm.result",index_col=0)


# In[31]:


df3["KO ID"] = df3["KO ID"].str.replace("KO:","").str.replace("_.*","")
df4 = df3[["KO ID","HMM ID"]]


df5 = pd.DataFrame(df4["KO ID"].str.split(',').tolist(), index=df4["HMM ID"]).stack() ##transform hmmID count to KO counts
df5 = df5.reset_index()[[0, "HMM ID"]]
df5.columns = ["KO ID","HMM ID"]

df6 = pd.DataFrame(df5.groupby("KO ID").size())
df6.columns = ["Counts"]
df6.to_csv(file_name.split(".")[0] +"_filtered_hmm.summary")


# In[1]:


#df_sum["KO ID"].str.replace("KO:","").str.replace("_.*,",",").str.replace("_.*","")

