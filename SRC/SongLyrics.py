#!/usr/bin/env python
# coding: utf-8

# In[89]:


#First Album
filenamesA1 = ['lyrics_billieeilish_badguy.txt', 'lyrics_billieeilish_xanny.txt','lyrics_billieeilish_youshouldseemeinacrown.txt', 'lyrics_billieeilish_allthegoodgirlsgotohell.txt', 'lyrics_billieeilish_wishyouweregay.txt', 'lyrics_billieeilish_whenthepartysover.txt', 'lyrics_billieeilish_8.txt', 'lyrics_billieeilish_mystrangeaddiction.txt', 'lyrics_billieeilish_buryafriend.txt', 'lyrics_billieeilish_ilomilo.txt', 'lyrics_billieeilish_listenbeforeigo.txt', 'lyrics_billieeilish_iloveyou.txt', 'lyrics_billieeilish_goodbye.txt']
with open('/Users/graceberrien23/Desktop/billie/newBillie.csv', 'w') as outfile:
    for fname in filenamesA1:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


# In[90]:


import pandas as pd


# In[92]:


baillieA1 = pd.read_csv('/Users/graceberrien23/Desktop/billie/newBillie.csv', sep = "NaN")


# In[93]:


billieA1
#billieA1.columns


# In[94]:


billie2A1 = billieA1['{'].str.split(":")


# In[95]:


#billie3A1 = billieA1[billieA1["{"].str.contains("lyrics")]


# In[97]:


#pd.set_option('display.max_rows', 500)
#billie3A1


# In[106]:


billie4A1 = billie3A1['{'].str.split(":")


# In[157]:


#lyricsA1 = billie4A1.iloc[5] + billie4A1.iloc[11] + billie4A1.iloc[17] + billie4A1.iloc[23] + billie4A1.iloc[29] + billie4A1.iloc[35] + billie4A1.iloc[41]

#for i in length(billie4A1):




# print(lyricsA1)

# In[143]:


#newLyr = [i.split('\n', 1)[0] for i in lyricsA1]
#ewNewLyr = [i.split('\ ', 1)[0] for i in newLyr]


# In[145]:


newLyr


# In[153]:


df = pd.DataFrame(billie4A1) 


# In[154]:


df.to_excel("/Users/graceberrien23/Desktop/billie/A1Billie.xlsx")


# In[159]:


#pip install PyLyrics


# In[162]:


#Second Album
filenamesA2 = ['lyrics_billieeilish_gettingolder.txt', 'lyrics_billieeilish_ididntchangemynumber.txt','lyrics_billieeilish_billiebossanova.txt', 'lyrics_billieeilish_myfuture.txt', 'lyrics_billieeilish_oxytocin.txt', 'lyrics_billieeilish_goldwing.txt', 'lyrics_billieeilish_lostcause.txt', 'lyrics_billieeilish_halleyscomet.txt', 'lyrics_billieeilish_notmyresponsibility.txt', 'lyrics_billieeilish_overheated.txt', 'lyrics_billieeilish_everybodydies.txt', 'lyrics_billieeilish_yourpower.txt', 'lyrics_billieeilish_nda.txt', 'lyrics_billieeilish_thereforeiam.txt', 'lyrics_billieeilish_happierthanever.txt', 'lyrics_billieeilish_malefantasy.txt']
with open('/Users/graceberrien23/Desktop/billie/BillieA2.csv', 'w') as outfile:
    for fname in filenamesA2:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


# In[165]:


billieA2 = pd.read_csv('/Users/graceberrien23/Desktop/billie/BillieA2.csv', sep = "NaN")


# In[166]:


billie2A2 = billieA2['{'].str.split(":")


# In[168]:


df2 = pd.DataFrame(billie2A2) 


# In[170]:


df2.to_excel("/Users/graceberrien23/Desktop/billie/A2Billie.xlsx")


# In[ ]:




