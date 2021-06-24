from time import sleep
import random
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

# to make firefox not run in headless mode, comment out the next two lines of code.
options = Options()
options.headless = True

browser = webdriver.Firefox()
likeCount = dislikeCount = followCount = unfollowCount = commentCount = profileCount = 0

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
    def tag(hash):
        sleep(1)
        browser.get('https://www.instagram.com/explore/tags/{}/'.format(hash))

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
    # goes to instagram.
    def startIG():
        browser.get('https://www.instagram.com/')

    # logs into instagram.
    def login(username, password):
        loginPage.login('{}'.format(username), '{}'.format(password))
        feed.sayNo()
        # feed.sayYes()

    # quits the browser after waiting a while.
    def stopIG(wait):
        print("Likes: ", likeCount, "\n",
        "Dislikes: ", dislikeCount, "\n",
        "Follows: ", followCount, "\n",
        "Unfollows: ", unfollowCount, "\n",
        "Comments: ", commentCount, "\n",
        "Profiles: ", profileCount, "\n")
        sleep(wait)
        browser.quit()

    # likes posts in home page.
    def likeHome(num):
        action.homLike(num)
        likeCount += 1
        action.scroll('top')

    # dislikes posts in home page.
    def dislikeHome(num):
        action.homDislike(num)
        dislikeCount += 1
        action.scroll('top')

    # follows suggested accounts.
    def suggestedFollow(numprof):
        for i in range(0, numprof):
            feed.suggestion()
            action.sugFollow(i + 1)
            profileCount += 1
            # if going into the profiles each time is not required,
            # then just loop the line below and comment out the rest up till feed.home().
            # action.sugFollow(fol)
            if (action.private() == 0):
                action.follow()
                sleep(120)
                browser.refresh()
                sleep(1)
                if (action.private() == 1):
                    followCount += 1
                    action.postSelect()
                    action.postLike()
                    likeCount += 1
                    action.close()
                else:
                    action.unfollow()
            else:
                action.follow()
                followCount += 1
                action.postSelect()
                action.postLike()
                likeCount += 1
            action.close()
        feed.home()

    # follows specified profile.
    def profFollow(handle):
        feed.user(handle)
        profileCount += 1
        if (action.private() == 0):
            action.follow()
            sleep(120)
            browser.refresh()
            sleep(1)
            if (action.private() == 1):
                followCount += 1
                action.postSelect()
                action.postLike()
                likeCount += 1
                action.close()
            else:
                action.unfollow()
        else:
            action.follow()
            followCount += 1
            action.profSelect()
            action.postLike()
            likeCount += 1
            action.close()
        feed.home()

    # unfollows accounts from following page.
    def ownUnfollow(numprof):
        feed.profile()
        num = action.followingCount()
        action.profFollowing()
        if (numprof == 'all'):
            for i in range(0, num):
                action.profUnfollow()
                unfollowCount += 1
        else:
            for i in range(0, numprof):
                action.profUnfollow()
                unfollowCount += 1
        feed.home()

    # comments on posts in the explore page.
    def exploreComment(num, text):
        feed.explore()
        action.expSelect()
        for i in range(0, num):
            action.comment(random.choice(text))
            commentCount += 1
            action.next()
        action.close()
        feed.home()

    # goes to accounts from posts in explore page and interacts with posts there.
    def exploreToProfile(num, numprof, text):
        for i in range(0, numprof):
            feed.explore()
            action.expSelect()
            sleep(1)
            for k in range(0, i):
                action.next()
            action.postToProf()
            profileCount += 1
            action.postSelect()
            for j in range(0, num):
                action.postLike()
                likeCount += 1
                action.comment(random.choice(text))
                commentCount += 1
                action.next()
            action.close()
        feed.home()

    # comments on posts in the top section of a tag page.
    def tagTopComment(hash, num, text):
        feed.tag(hash)
        action.topSelect()
        for i in range(0, num):
            action.comment(random.choice(text))
            commentCount += 1
            action.next()
        action.close()
        feed.home()

    # comments on posts in the recent section of a tag page.
    def tagRecComment(hash, num, text):
        feed.tag(hash)
        action.recSelect()
        for i in range(0, num):
            action.postLike()
            likeCount += 1
            action.comment(random.choice(text))
            commentCount += 1
            action.next()
        action.close()
        feed.home()

    # goes to accounts from posts in a tag page and interacts with posts there.
    def tagToProfile(hash, num, numprof, text):
        for i in range(0, numprof):
            feed.tag(hash)
            # action.recSelect()
            action.topSelect()
            sleep(1)
            for k in range(0, i):
                action.next()
            action.postToProf()
            profileCount += 1
            action.postSelect()
            for j in range(0, num):
                action.postLike()
                likeCount += 1
                action.next()
            action.comment(random.choice(text))
            commentCount += 1
            action.close()
        feed.home()

    # goes to top profiles directory and interacts with accounts there.
    def topProfile(num, numprof, text):
        for i in range(1, numprof + 1):
            feed.topAcc()
            action.topAccounts(i)
            profileCount += 1
            for j in range(0, num):
                action.postSelect()
                sleep(1)
                action.comment(random.choose(text))
                commentCount += 1
                action.next()
            action.close()
        feed.home()

# class for basic instagram interactions.
class action:
    # clicks the like icon in home page.
    def homLike(n):
        for count in range(1, n + 1):
            sleep(4)
            try:
                like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
                like.click()
            except NoSuchElementException:
                pass
                print("Couldn't like post in homepage.")

    # clicks the dislike icon in home page.
    def homDislike(n):
        for count in range(1, n + 1):
            sleep(4)
            try:
                dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")
                dislike.click()
                # coordinates = dislike.location_once_scrolled_into_view
                # browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            except NoSuchElementException:
                pass
                print("Couldn't dislike post in homepage.")

    # clicks the like button in posts.
    def postLike():
        sleep(1)
        try:
            like = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Like'][@height = '24']")
            like.click()
        except NoSuchElementException:
            pass
            print("Couldn't like post.")

    # clicks the dislike button in posts.
    def postDislike():
        sleep(1)
        try:
            dislike = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Unlike'][@height = '24']")
            dislike.click()
        except NoSuchElementException:
            pass
            print("Couldn't dislike post.")

    # comments on posts.
    def comment(text):
        sleep(1)
        try:
            sleep(1)
            comment = browser.find_element_by_xpath("//textarea")
            comment.click()
            comment = browser.find_element_by_xpath("//textarea")
            comment.send_keys(text)
            comment.send_keys(Keys.ENTER)
        except StaleElementReferenceException:
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
        except NoSuchElementException:
            pass
            print("Couldn't comment on post.")

    # clicks the first picture in the profile page.
    def postSelect():
        sleep(1)
        try:
            select = browser.find_element_by_xpath("//article/div/div/div/div")
            select.click()
        except NoSuchElementException:
            pass
            print("Couldn't select post in profile page.")

    # clicks the first picture in the explore page.
    def expSelect():
        sleep(2)
        try:
            select = browser.find_element_by_xpath("//main/div/div/div/div/div[2]")
            select.click()
        except NoSuchElementException:
            pass
            print("Couldn't find post in explore page.")

    # clicks the first top post of a tag.
    def topSelect():
        sleep(2)
        try:
            select = browser.find_element_by_xpath("//article/div/div/div/div/div")
            select.click()
        except NoSuchElementException:
            pass
            print("Couldn't find top post in tag page.")

    # clicks the first recent post of a tag.
    def recSelect():
        sleep(2)
        try:
            select = browser.find_element_by_xpath("//article/div[2]/div/div/div")
            select.click()
        except NoSuchElementException:
            pass
            print("Couldn't find recent post in tag page.")

    # clicks the next button on a post in a profile.
    def next():
        sleep(2)
        try:
            next = browser.find_element_by_xpath("//a[contains(.,'Next')]")
            next.click()
        except NoSuchElementException:
            pass
            print("Couldn't find next button.")

    # clicks the previous button on a post in a profile.
    def prev():
        sleep(2)
        try:
            prev = browser.find_element_by_xpath("//a[contains(.,'Next')]")
            prev.click()
            return 0
        except NoSuchElementException:
            pass
            print("Couldn't find previous button.")

    # clicks the close button on a post in a profile.
    def close():
        sleep(1)
        try:
            close = browser.find_element_by_xpath("//*[name() = 'svg'][@aria-label = 'Close']")
            close.click()
        except NoSuchElementException:
            pass
            print("Couldn't find close button.")

    # scrolls to the top if specified, otherwise goes 400px downwards.
    def scroll(dir):
        sleep(1)
        if (dir == 'top'):
            browser.execute_script('window.scrollTo(0, 0);')
        else:
            browser.execute_script('window.scrollTo(0, 400);')

    # returns number of posts of user.
    def postCount():
        sleep(1)
        posts = browser.find_element_by_xpath("//li/span/span")
        num = BS(posts.get_attribute('innerHTML'), 'html.parser').text
        return num

    # clicks the follow button in any user's page.
    def follow():
        sleep(1)
        try:
            follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        except NoSuchElementException:
            pass
            print("Couldn't find follow button.")

    # clicks the unfollow button in unfollow prompt.
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
            print("Couldn't find unfollow button.")

    # clicks the follow button in suggestion page if parameter is 'fol' ,otherwise it goes into their profiles.
    def sugFollow(n):
        # coordinates = follow.location_once_scrolled_into_view
        # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        if (n == 'fol'):
            sleep(1)
            follow = browser.find_element_by_xpath("//button[contains(.,'Follow')]")
            follow.click()
        else:
            sleep(1)
            try:
                profile = browser.find_element_by_xpath("div[n]/div[2]/div/div/span/a")
                profile.click()
            except NoSuchElementException:
                pass
                print("Couldn't find follow button in suggestions page.")

    # checks if there's a "Account is private" tag.
    def private():
        sleep(1)
        try:
            private = browser.find_element_by_xpath("//h2[contains(.,'Private')]")
            return 0
        except NoSuchElementException:
            return 1

    # returns number of accounts the user follows.
    def followingCount():
        sleep(1)
        following = browser.find_element_by_xpath("//li[3]/a/span")
        num = BS(following.get_attribute('innerHTML'), 'html.parser').text
        return num

    # returns number of accounts that follow the user.
    def followerCount():
        sleep(1)
        following = browser.find_element_by_xpath("//li[2]/a/span")
        num = BS(follower.get_attribute('innerHTML'), 'html.parser').text
        return num

    # clicks the following button in profile.
    def profFollowing():
        sleep(1)
        try:
            following = browser.find_element_by_xpath("//a[text() = ' following']")
            following.click()
        except NoSuchElementException:
            pass
            print("Couldn't find the following button in profile.")

    # clicks the unfollow button in own following page.
    def profUnfollow():
        sleep(2)
        try:
            following = browser.find_element_by_xpath("//button[text() = 'Following']")
            following.click()
        except NoSuchElementException:
            pass
            print("Couldn't find following button.")
        sleep(1)
        try:
            unfollow = browser.find_element_by_xpath("//button[text() = 'Unfollow']")
            unfollow.click()
        except NoSuchElementException:
            pass
            print("Couldn't find unfollow button.")
        # coordinates = unfollow.location_once_scrolled_into_view
        # browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))

    # clicks the username of the post uploader when post is selected.
    def postToProf():
        sleep(1)
        try:
            profimg = browser.find_element_by_xpath("//a/img")
            profimg.click()
        except NoSuchElementException:
            pass
            print("Couldn't find username in post.")

    # clicks the top profiles sequentially.
    def topAccounts(num):
        sleep(1)
        try:
            prof = browser.find_element_by_xpath("//li[num]/a")
            prof.click()
        except NoSuchElementException:
            pass
            print("Couldn't find account in top profiles.")
