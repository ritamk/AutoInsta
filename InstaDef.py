from time import sleep
import random
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# class for login page actions.
class loginPage:
    # logs in with provided username, password and returns to feed (next page after loginPage).
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

# class for feed page actions.
class feed:
    # selects "No" when prompted if the browser should remember the login details.
    def sayNo():
        sleep(2)
        forgetLogin = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        forgetLogin.click()
        sleep(2)
        noNotif = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()

    # selects "Yes" when prompted if the browser should remember the login details.
    def sayYes():
        sleep(2)
        rememberLogin = browser.find_element_by_xpath("//button[contains(.,'Save Info')]")
        rememberLogin.click()
        sleep(2)
        noNotif = browser.find_element_by_xpath("//button[contains(.,'Not Now')]")
        noNotif.click()

    # goes to home page.
    def home():
        sleep(1)
        profPage = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Home']")
        profPage.click()

    # goes to my profile page.
    def profile():
        sleep(1)
        profPage = browser.find_element_by_xpath("//img[@alt = contains(.,'profile picture')]")
        profPage.click()

    # goes to profile page of specified user.
    def user(name):
        sleep(1)
        browser.get('https://www.instagram.com/{}/'.format(name))

    # goes to the explore page.
    def explore():
        sleep(1)
        expPage = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Find People']")
        expPage.click()

    # goes to the explore page of specified tag.
    def tag(tag):
        sleep(1)
        browser.get('https://www.instagram.com/explore/tags/{}/'.format(tag))

    # goes to the suggested people to follow page.
    def suggestion():
        sleep(1)
        browser.get('https://www.instagram.com/explore/people/suggested/')

    # goes to the top profiles page.
    def topAcc():
        sleep(1)
        browser.get('https://www.instagram.com/directory/profiles/0-0/')

# performs functions the user specifies
class do:
    def startIG():
        browser.get('https://www.instagram.com/')

    def login(username, password):
        loginPage.login('{}'.format(username), '{}'.format(password))
        feed.sayNo()

    def stopIG(wait):
        sleep(wait)
        browser.quit()

    def likeHome(num):
        action.homLike(num)
        action.scroll('top')

    def dislikeHome(num):
        action.homDislike(num)
        action.scroll('top')

    def suggestedFollow(numprof):
        for i in range(0, numprof0):
            feed.suggestion()
            action.sugProf(i + 1)
            if (action.private() == 0):
                action.follow()
                sleep(60)
                browser.refresh()
                sleep(1)
                if (action.private() == 1):
                    action.postSelect()
                    action.postLike()
                    action.close()
                else:
                    action.unfollow()
            else:
                action.follow()
                action.postSelect()
                action.postLike()
            action.close()
        feed.home()

    def profFollow(handle):
        feed.user(handle)
        if (action.private() == 0):
            action.follow()
            sleep(3)
            browser.refresh()
            sleep(1)
            if (action.private() == 1):
                action.postSelect()
                action.postLike()
                action.close()
            else:
                action.unfollow()
        else:
            action.follow()
            action.profSelect()
            action.postLike()
            action.close()
        sleep(2)
        feed.home()

    def ownUnfollow(numprof):
        feed.profile()
        action.profFollowing()
        num = action.followingCount()
        for i in range(0, num):
            action.profUnfollow()
        feed.home()

    def exploreComment(num, text):
        feed.explore()
        action.expSelect()
        for i in range(0, num):
            action.comment(random.choice(text))
            action.next()
        action.close()
        feed.home()

    def exploreToProfile(num, numprof, text):
        for i in range(0, numprof):
            feed.explore()
            action.expSelect()
            sleep(1)
            for k in range(0, i):
                action.next()
            action.postToProf()
            action.postSelect()
            for j in range(0, num):
                action.postLike()
                action.comment(random.choice(text))
                action.next()
            action.close()
        feed.home()

    def tagTopComment(hash, num, text):
        feed.tag(hash)
        action.topSelect()
        for i in range(0, num):
            action.comment(random.choice(text))
            action.next()
        action.close()
        feed.home()

    def tagRecComment(hash, num, text):
        feed.tag(hash)
        action.recSelect()
        for i in range(0, num):
            action.postLike()
            action.comment(random.choice(text))
            action.next()
        action.close()
        feed.home()

    def tagToProfile(hash, num, numprof, text):
        for i in range(0, numprof):
            feed.tag(hash)
            action.topSelect()
            sleep(1)
            for k in range(0, i):
                action.next()
            action.postToProf()
            action.postSelect()
            for j in range(0, num):
                action.postLike()
                action.next()
            action.comment(random.choice(text))
            action.close()
        feed.home()

    def topProfile(num, numprof, text):
        for i in range(1, numprof + 1):
            feed.topAcc()
            action.topAccounts(i)
            for j in range(0, num):
                action.postSelect()
                sleep(1)
                action.comment(random.choose(text))
                action.next()
            action.close()
        feed.home()

# class for basic instagram interactions.
class action:
    # clicks the follow button in suggestion page if parameter is 'fol' ,otherwise it goes into their profiles.
    def sugProf(n):
        # coordinates = follow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        if (n == 'fol'):
            sleep(1)
            follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        else:
            sleep(1)
            profile = browser.find_element_by_xpath("div[n]/div[2]/div/div/span/a")
            profile.click()

    # clicks the follow button in any user's page.
    def follow():
        sleep(1)
        try:
            follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        except NoSuchElementException:
            pass

    def unfollow():
        sleep(1)
        try:
            unf = browser.find_element_by_xpath("//button[contains(.,'Unfollow')]")
            unf.click()
        except NoSuchElementException:
            req = browser.find_element_by_xpath("//button[contains(.,'Requested')]")
            req.click()
            sleep(1)
            unf = browser.find_element_by_xpath("//button[contains(.,'Unfollow')]")
            unf.click()
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
        unfollow = browser.find_element_by_xpath("//button[text() = 'Following']")
        following.click()
        sleep(1)
        unfollow = browser.find_element_by_xpath("//button[text() = 'Unfollow']")
        # coordinates = unfollow.location_once_scrolled_into_view
        # browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        unfollow.click()

    # clicks the like icon in home page.
    def homLike(n):
        for count in range(1, n + 1):
            sleep(4)
            like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
            like.click()

    # clicks the dislike icon in home page.
    def homDislike(n):
        for count in range(1, n + 1):
            sleep(4)
            dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")
            # coordinates = dislike.location_once_scrolled_into_view
            # browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            dislike.click()

    # clicks the like button in posts.
    def postLike():
        sleep(1)
        try:
            like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
            like.click()
        except NoSuchElementException:
            pass

    # clicks the dislike button in posts.
    def postDislike():
        sleep(1)
        try:
            dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")
            dislike.click()
        except NoSuchElementException:
            pass

    # comments on posts.
    def comment(text):
        sleep(2)
        try:
            sleep(1)
            comment = browser.find_element_by_xpath("//textarea")
            comment.click()
            comment = browser.find_element_by_xpath("//textarea")
            comment.send_keys(text)
            comment.send_keys(Keys.ENTER)
        except NoSuchElementException:
            sleep(1)
            pause = browser.find_element_by_xpath("//div[@aria-label = 'Control']")
            pause.click()
            sleep(1)
            comment = browser.find_element_by_xpath("//textarea")
            comment.click()
            sleep(1)
            comment = browser.find_element_by_xpath("//textarea")
            comment.send_keys(text)
            comment.send_keys(Keys.ENTER)
        except:
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
        sleep(2)
        # try:
        next = browser.find_element_by_xpath("//a[contains(.,'Next')]")
        next.click()
        return 0
        # except NoSuchElementException:
        #     return 1
        #     pass

    # clicks the previous button on a post in a profile.
    def prev():
        sleep(2)
        try:
            prev = browser.find_element_by_xpath("//a[contains(.,'Next')]")
            prev.click()
            return 0
        except NoSuchElementException:
            return 1
            pass

    # clicks the close button on a post in a profile.
    def close():
        sleep(1)
        try:
            close = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Close']")
            close.click()
        except NoSuchElementException:
            pass

    # returns number of posts of user.
    def postCount():
        sleep(1)
        posts = browser.find_element_by_xpath("//li/span/span")
        num = BS(posts.get_attribute('innerHTML'), 'html.parser').text
        return num

    def followingCount():
        sleep(1)
        following = browser.find_element_by_xpath("//li[3]/a/span")
        num = BS(following.get_attribute('innerHTML'), 'html.parser').text
        return num

    def followerCount():
        sleep(1)
        following = browser.find_element_by_xpath("//li[2]/a/span")
        num = BS(follower.get_attribute('innerHTML'), 'html.parser').text
        return num

    # scrolls to the top if specified, otherwise goes 400px downwards.
    def scroll(dir):
        sleep(1)
        if (dir == 'top'):
            browser.execute_script('window.scrollTo(0, 0);')
        else:
            browser.execute_script('window.scrollTo(0, 400);')

    # clicks the top profiles sequentially
    def topAccounts(num):
        sleep(1)
        prof = browser.find_element_by_xpath("//li[num]/a")
        prof.click()
