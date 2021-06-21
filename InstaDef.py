from time import sleep
import random
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# class for login page actions.
class loginPage:
    # logs in with provided username, password and returns to feedPage (next page after loginPage).
    def login(username, password):
        browser.implicitly_wait(5)
        usernameInput = browser.find_element_by_css_selector("input[name = 'username']")
        passwordInput = browser.find_element_by_css_selector("input[name = 'password']")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        # loginTap = self.browser.find_element_by_xpath("//div[text() = 'Log In']")
        # loginTap.click()
        return feedPage()

# class for feed page actions.
class feedPage:
    # selects "No" when prompted if the browser should remember the login details.
    def sayNo():
        sleep(1)
        forgetLogin = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        forgetLogin.click()
        sleep(1)
        noNotif = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()

    # selects "Yes" when prompted if the browser should remember the login details.
    def sayYes():
        sleep(1)
        rememberLogin = browser.find_element_by_xpath("//button[contains(.,'Save Info')]")
        forgetLogin.click()
        sleep(1)
        noNotif = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()

    # # goes to home page.
    # def home(self):
    #     sleep(2)
    #     profPage = self.browser.get('https://www.instagram.com/')
    #     return do(self.browser)
    #
    # # goes to my profile page.
    # def profile(self):
    #     sleep(2)
    #     profPage = self.browser.get('https://www.instagram.com/ritamksth/')
    #     return do(self.browser)
    #
    # # goes to profile page of specified user.
    # def user(self, name):
    #     sleep(2)
    #     profPage = self.browser.get('https://www.instagram.com/{}/'.format(name))
    #     return do(self.browser)
    #
    # # goes to the explore page.
    # def explore(self):
    #     sleep(2)
    #     tagPage = self.browser.get('https://www.instagram.com/explore/')
    #     return do(self.browser)
    #
    # # goes to the explore page of specified tag.
    # def tag(self, tag):
    #     sleep(2)
    #     tagPage = self.browser.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    #     return do(self.browser)
    #
    # # goes to the suggested people to follow page.
    # def suggestion(self):
    #     sleep(2)
    #     sugnPage = self.browser.get('https://www.instagram.com/explore/people/suggested/')
    #     return do(self.browser)

# performs functions the user specifies
class do:
    def startIG():
        browser.get('https://www.instagram.com/')

    def login(username, password):
        prompt = loginPage.login('{}'.format(username), '{}'.format(password))
        prompt.sayNo()

    def stopIG(wait):
        sleep(wait)
        browser.quit()

    def likeHome(num):
        action.homLike()
        action.scroll('top')

    def dislikeHome(num):
        action.homDislike(num)
        action.scroll('top')

    def suggestedFollow(num):
        sug = browser.get('https://www.instagram.com/explore/people/suggested')
        for i in range(0, num):
            action.sugFollow()
        action.feed()

    def exploreComment(num, text):
        exp = browser.get('https://www.instagram.com/explore/')
        action.expSelect()
        for i in range(0, num):
            com = random.choice(text)
            action.comment(com)
            action.next()
        action.close()
        action.feed()

# class for basic instagram interactions.
class action:
    # clicks the follow button in suggestion page.
    def sugFollow():
        sleep(1)
        follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
        # coordinates = follow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        follow.click()

    # clicks the follow button in any user's page.
    def follow():
        sleep(1)
        try:
            follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        except NoSuchElementException:
            pass

    # checks if there's a "Account is private" tag.
    def private():
        sleep(1)
        try:
            private = browser.find_element_by_xpath("//h2[contains(.,'Private')]")
            return 0
        except NoSuchElementException:
            return 1

    # clicks the following button in profile.
    def profFollowing():
        sleep(2)
        following = browser.find_element_by_xpath("//a[text() = ' following']")
        following.click()

    # clicks the unfollow button in own following page.
    def profUnfollow():
        sleep(2)
        following = unfollow = browser.find_element_by_xpath("//button[text() = 'Following']")
        following.click()
        sleep(1)
        unfollow = browser.find_element_by_xpath("//button[text() = 'Unfollow']")
        # coordinates = unfollow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        unfollow.click()

    # clicks the like icon in home page.
    def homLike(n):
        for count in range(1, n + 1):
            sleep(4)
            like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
            # coordinates = like.location_once_scrolled_into_view
            # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            like.click()

    # clicks the dislike icon in home page.
    def homDislike(n):
        for count in range(1, n + 1):
            sleep(4)
            dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")

    # clicks the like button in posts.
    def postLike():
        sleep(1)
        like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
        like.click()

    # clicks the dislike button in posts.
    def postDislike():
        sleep(1)
        dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")
        dislike.click()

    # comments on posts.
    def comment(text):
        sleep(2)
        try:
            comment = browser.find_element_by_xpath("//textarea")
            comment.click()
            comment = browser.find_element_by_xpath("//textarea")
            comment.send_keys(text)
            comment.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

    # clicks the first picture in the profile page.
    def postSelect():
        sleep(1)
        try:
            select = browser.find_element_by_xpath("//article/div/div/div/div")
            select.click()
        except NoSuchElementException:
            pass

    # clicks the first picture in the explore page.
    def expSelect():
        sleep(2)
        select = browser.find_element_by_xpath("//main/div/div/div/div/div[2]")
        select.click()

    # clicks the first top post of a tag.
    def topSelect():
        sleep(2)
        select = browser.find_element_by_xpath("//article/div/div/div/div/div")
        select.click()

    # clicks the first recent post of a tag.
    def recSelect():
        sleep(2)
        select = browser.find_element_by_xpath("//article/div[2]/div/div/div")
        select.click()

    def postToProf():
        sleep(1)
        profimg = browser.find_element_by_xpath("//a/img")
        profimg.click()

    # clicks the next button on a post in a profile.
    def next():
        sleep(1)
        try:
            next = browser.find_element_by_xpath("//a[text() = 'Next']")
            next.click()
            return 0
        except NoSuchElementException:
            return 1

    # clicks the previous button on a post in a profile.
    def prev():
        sleep(1)
        next = browser.find_element_by_xpath("//a[text() = 'Previous']")
        next.click()

    # clicks the close button on a post in a profile.
    def close():
        sleep(1)
        try:
            close = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Close']")
            close.click()
        except NoSuchElementException:
            pass

    # clicks the home button.
    def feed():
        sleep(1)
        home = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Home']")
        home.click()

    # returns number of posts of user.
    def postCount():
        sleep(1)
        posts = browser.find_element_by_xpath("//li/span/span")
        num = BS(posts.get_attribute('innerHTML'), 'html.parser').text
        return num

    def scroll(dir):
        sleep(1)
        if (dir == 'top'):
            browser.execute_script('window.scrollTo(0, 0);')
        else:
            browser.execute_script('window.scrollTo(0, 400);')
