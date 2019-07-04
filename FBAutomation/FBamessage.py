
# coding: utf-8

# In[10]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


# In[11]:


#Variables
name = ""
msg = ""
email = ""
password = ""




def askDetails():
    global name,msg,email,password
    email = input("Enter your email ")
    password = input("Enter your password ")
    name = input("Enter name whom to message ")
    msg = input("Enter the message body ")
    
    


# In[12]:


def openPage():
    web.get("https://www.facebook.com/")


# In[13]:


def openFbId():
    time.sleep(5)
    emailArea = web.find_element_by_id('email')
    emailArea.send_keys(email)
    passwordArea = web.find_element_by_id('pass')
    passwordArea.send_keys(password)
    login = web.find_element_by_id('loginbutton')
    time.sleep(2)
    login.click()


# In[14]:


def search():
    time.sleep(5)
    search = web.find_element_by_css_selector('input._58al')
    search.send_keys(name)
    time.sleep(3)
    search = web.find_element_by_css_selector('input._58al')
    search.send_keys(Keys.RETURN)
def sendmessage():
    time.sleep(5)
    actions = ActionChains(web)
    actions.send_keys(msg)
    actions.send_keys(Keys.RETURN)
    actions.perform()



# In[15]:


def close():
    first = web.find_element_by_id('userNavigationLabel')
    first.click()
    time.sleep(2)
    logoutMenu =web.find_elements_by_class_name('_54nh')
    logoutMenu[8].click()

    


# In[17]:


web = webdriver.Chrome(executable_path=r"C:\Users\Param\Anaconda3\chromedriver_win32\chromedriver.exe")
askDetails()
openPage()
openFbId()
search()
sendmessage()
close()



# In[18]:


web.close()

