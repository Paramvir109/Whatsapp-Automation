
# coding: utf-8

# In[5]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

#Variables
name = ""
msg = ""
noOfTimes = 0


# In[6]:


def askDetails():
    global name,msg,noOfTimes #This is how to refer to global var. Values will persist b/w function calls
    name = input("Enter name whom to message ")
    msg = input("Enter the message body ")
    noOfTimes = int(input("Enter the no. of times you want to send the message "))
    


# In[7]:


def openPage():
    web.get('https://web.whatsapp.com/')



# In[8]:


def searchChat():
    search=web.find_element_by_css_selector("[title='Search or start new chat']")
    search.send_keys(name)
    time.sleep(1)
    nextS=web.find_element_by_css_selector("span[title=" + name + "]")
    nextS.click()


# In[9]:


def sendMessage():
    actions = ActionChains(web)
    for i in range(0,noOfTimes):
        actions.send_keys(msg)
        actions.send_keys(Keys.RETURN)
    actions.perform()
    


# In[12]:


web = webdriver.Chrome(executable_path=r"C:\Users\Param\Anaconda3\chromedriver_win32\chromedriver.exe")
#replace the above path with your chromedriver path
askDetails()
openPage()
time.sleep(6)
searchChat()
time.sleep(2)
sendMessage()


# In[ ]:





# In[ ]:





# In[ ]:




