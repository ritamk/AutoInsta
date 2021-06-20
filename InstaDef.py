from time import sleep
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# class for login page actions.
class loginPage:
    def __init__(self, browser):
        self.browser = browser

    # logs in with provided username, password and returns to feedPage (next page after loginPage).
    def login(self, username, password):
        usernameInput = self.browser.find_element_by_css_selector("input[name = 'username']")
        passwordInput = self.browser.find_element_by_css_selector("input[name = 'password']")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        # loginTap = self.browser.find_element_by_xpath("//div[text() = 'Log In']")
        # loginTap.click()
        return feedPage(self.browser)

# class for feed page actions.
class feedPage:
    def __init__(self, browser):
        self.browser = browser

    # selects "No" when prompted if the browser should remember the login details.
    def sayNo(self):
        sleep(1)
        forgetLogin = self.browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        forgetLogin.click()
        sleep(1)
        noNotif = self.browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()
        return action(self.browser)

    # selects "Yes" when prompted if the browser should remember the login details.
    def sayYes(self):
        sleep(1)
        rememberLogin = self.browser.find_element_by_xpath("//button[contains(.,'Save Info')]")
        forgetLogin.click()
        sleep(1)
        noNotif = self.browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()
        return action(self.browser)

    # goes to home page.
    def home(self):
        sleep(2)
        profPage = self.browser.get('https://www.instagram.com/')
        return action(self.browser)

    # goes to my profile page.
    def profile(self):
        sleep(2)
        profPage = self.browser.get('https://www.instagram.com/ritamksth/')
        return action(self.browser)

    # goes to profile page of specified user.
    def user(self, name):
        sleep(2)
        profPage = self.browser.get('https://www.instagram.com/{}/'.format(name))
        return action(self.browser)

    # goes to the explore page.
    def explore(self):
        sleep(2)
        tagPage = self.browser.get('https://www.instagram.com/explore/')
        return action(self.browser)

    # goes to the explore page of specified tag.
    def tag(self, tag):
        sleep(2)
        tagPage = self.browser.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
        return action(self.browser)

    # goes to the suggested people to follow page.
    def suggestion(self):
        sleep(2)
        sugnPage = self.browser.get('https://www.instagram.com/explore/people/suggested/')
        return action(self.browser)

# class for basic instagram interactions.
class action:
    def __init__(self, browser):
        self.browser = browser

    # clicks the follow button in suggestion page.
    def sugFollow(self):
        sleep(2)
        follow = self.browser.find_element_by_xpath("//button[contains(.,'Follow')]")
        # coordinates = follow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        follow.click()

    # clicks the follow button in any user's page.
    def follow(self):
        sleep(2)
        try:
            follow = self.browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        except NoSuchElementException:
            pass

    # checks if there's a "Account is private" tag.
    def private(self):
        sleep(1)
        try:
            private = self.browser.find_element_by_xpath("//h2[contains(.,'Private')]")
            return 0
        except NoSuchElementException:
            return 1

    # clicks the following button in profile.
    def profFollowing(self):
        sleep(2)
        following = self.browser.find_element_by_xpath("//a[text() = ' following']")
        following.click()

    # clicks the unfollow button in own following page.
    def profUnfollow(self):
        sleep(2)
        following = unfollow = self.browser.find_element_by_xpath("//button[text() = 'Following']")
        following.click()
        sleep(1)
        unfollow = self.browser.find_element_by_xpath("//button[text() = 'Unfollow']")
        # coordinates = unfollow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        unfollow.click()

    # clicks the like icon in home page.
    def homLike(self, n):
        for count in range(1, n + 1):
            sleep(1)
            like = self.browser.find_element_by_xpath("//article[{}]/div[3]/section/span/button" .format(count))
            coordinates = like.location_once_scrolled_into_view
            self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            like.click()

    # clicks the dislike icon in home page.
    def homDislike(self, n):
        for count in range(1, n + 1):
            sleep(1)
            dislike = self.browser.find_element_by_xpath("//article[{}]/div[3]/section/span/button".format(count))
            coordinates = dislike.location_once_scrolled_into_view
            self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            dislike.click()

    # clicks the like button in posts.
    def postLike(self):
        sleep(1)
        like = self.browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like']")
        like.click()

    # clicks the dislike button in posts.
    def postDislike(self):
        sleep(1)
        dislike = self.browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike']")
        dislike.click()

    # comments on posts.
    def comment(self, text):
        sleep(1)
        try:
            comment = self.browser.find_element_by_xpath("//form/textarea[text() = 'Add a comment ']")
            comment.send_keys(text)
            comment.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

    # clicks the first picture in the profile page.
    def postSelect(self):
        sleep(2)
        try:
            select = self.browser.find_element_by_xpath("//article/div/div/div/div")
            select.click()
        except NoSuchElementException:
            pass

    # clicks the first picture in the explore page.
    def expSelect(self):
        sleep(2)
        select = self.browser.find_element_by_xpath("//ul")
        select.click()

    # clicks the first top post of a tag.
    def topSelect(self):
        sleep(2)
        select = self.browser.find_element_by_xpath("//ul")
        select.click()

    # clicks the first recent post of a tag.
    def recSelect(self):
        sleep(2)
        text = self.browser.find_element_by_xpath("//h2[text() = 'Most Recent']")
        text.click()
        sleep(1)
        select = self.browser.find_element_by_xpath("//ul")
        select.click()

    # clicks the next button on a post in a profile.
    def next(self):
        sleep(1)
        try:
            next = self.browser.find_element_by_xpath("//a[text() = 'Next']")
            next.click()
            return 0
        except NoSuchElementException:
            return 1

    # clicks the previous button on a post in a profile.
    def prev(self):
        sleep(1)
        next = self.browser.find_element_by_xpath("//a[text() = 'Previous']")
        next.click()

    # clicks the close button on a post in a profile.
    def close(self):
        sleep(1)
        try:
            close = self.browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Close']")
            close.click()
        except NoSuchElementException:
            pass

    # clicks the home button.
    def feed(self):
        sleep(1)
        home = self.browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Home']")
        home.click()

    # returns number of posts of user.
    def postCount(self):
        sleep(1)
        posts = self.browser.find_element_by_xpath("//li/span/span")
        num = bs(posts.get_attribute('innerHTML'), 'html.parser').text
        return num