from time import sleep
from selenium import webdriver
import InstaDef

# initialises the browser.
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
browser.implicitly_wait(5)

# variable initialisation.
i = 0
profLikeCount = 20
homLikeCount = 5
sugFollowCount = 9

# running the task.
loggingIn = InstaDef.loginPage(browser)
feed = loggingIn.login("ritamksth", "sh0rtp@5s")
feed.sayNo()
handle = feed.user("ritamwho")
handle.follow()
if (handle.private() == 0):
    sleep(30)
    browser.refresh()
handle.postSelect()
while (i < int(handle.postCount()) and i < profLikeCount):
    handle.postLike()
    handle.next()
    i += 1
handle.close()
sleep(2)
handle.feed()

# waiting before quitting session.
sleep(20)
browser.quit()