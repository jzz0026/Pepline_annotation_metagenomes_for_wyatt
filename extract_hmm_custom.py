## python extract_hmm_custom.py the_whole_foam_data KO_list(one column of KO ID) output

from sys import argv
script, hmm_database, KO_list, outfile = argv





hmm_file = open(hmm_database) 
hmm_file =  hmm_file.read()


# In[ ]:


hmms = hmm_file.split("//")


# In[ ]:
## open KO list and read KO ID
KO_file = open(KO_list)
KO = KO_file.read()
KO_list = KO.split("\n")
KO_list = filter(None, KO_list)
names = filter(None, KO_list)

# In[ ]:


extracts = []
for each in names:
    extracts = extracts + [a for a in hmms if each in a]
extracts = set(extracts)


# In[ ]:


outfile = open(outfile,"w")
outfile.write('\n//\n'.join(extracts))
outfile.close()


# In[ ]:


#extracted_names = get_ipython().getoutput('cat extract_hmm.hmm | grep "KO:" | awk -F ":|_|," \'{print $2}\' | awk -F " " \'{print $1}\' | sort | uniq ')


# In[ ]:


#df2 = pd.DataFrame(extracted_names[1:])
#df2[1] = 1
#df3 = pd.merge(df,df2,left_on='KO',right_on=0,how="left")
#df4 = df3.iloc[:,[4,-1]]
#len(df4[df4.isnull().any(axis=1)])


# In[ ]:


#df5 = pd.merge(df,df2,left_on='KO',right_on=0,how="outer")
#df6 = df5.iloc[:,[4,-2,-1]]
#df6[df6.iloc[:,1].isnull()]

