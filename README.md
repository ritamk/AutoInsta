# AutoInsta
A side project, to simply help myself learn more about browser automation. The documentation is absolutely premature, just like the project itself. I will modify it once I'm happy with my progress at this. Below are brief descriptions of functions divided by classes in the [InstaDef.py](InstaDef.py) file.

<details>
	<summary>Do</summary>
    The do class contains the functions that interact with the user and utilise the other classes to get the complete the desired tasks. Below is a list of all the functions in this class and a brief description of what each one of them does.
	<br>
	</br>
	<ul>
		<!-- <li><i></i></li> -->
        <li><i>startIG()</i></li>
		This function is the one that starts the browser and goes to the instagram site.
        <li><i>login(username, password)</i></li>
        This function takes two parameters: username and password of the user. This is used to login to the site. It also selects 'No' when prompted about either saving login details or showing notifications.
        <li><i>stopIG(wait)</i></li>
        This function quits the browser. It takes one parameter: wait. This determines the number of seconds the browser should wait before quitting.
        <li><i>likeHome(num)</i></li>
        This function likes the posts on the home page. It takes one parameter: num, which determines the number of posts that are to be liked. After completing the task it scrolls back up to the top of the page.
        <li><i>dislikeHome(num)</i></li>
        This function dislikes the posts on the home page. It takes one parameter: num, which determines the number of posts that are to be disliked. After completing the task it scrolls back up to the top of the page.
        <li><i>suggestedFollow(numprof)</i></li>
        This function follows profiles in the suggested page. It can do so by either going into each profile and liking one post, or by simply following from the suggestions page itself.
		<li><i></i></li>
	</ul>
</details>

<details>
	<summary>Actions</summary>
    The action class contains functions that interact with the interface of the website. Below is a list of all the functions in this class and a brief description of what each of them does.
	<br>
	</br>
	<ul>
		<!-- <li><i></i></li> -->
		<li><i>homLike(n)</i></li>
		This function likes posts in the home/feed section of Instagram. It takes one parameter: n, this is the number of posts that the function will like before scrolling back up top. It waits for 4 seconds between each like, to make the activity seem more natural.
        <li><i>homDislike(n)</i></li>
		This function dislikes posts in the home/feed section of Instagram. It takes one parameter: n, this is the number of posts that the function will dislike before scrolling back up top. It waits for 4 seconds between each dislike.
        <li><i>postLike()</i></li>
		This function likes pop-up posts. It waits 1 second before doing so to let the elements load properly.
		<li><i>postDislike()</i></li>
		This function dislikes pop-up posts. It waits 1 second before doing so.
        <li><i>comment(text)</i></li>
		This function comments on pop-up posts. It takes a parameter: text, this is the text that is commented on a post. In a video, the function behaves abnormally. It waits at least 2 seconds before doing so. If it can't locate the commenting interface, it forfeits the action.
        <li><i>postSelect()</i></li>
		This function selects the first post in any account and opens it in pop-up mode. It waits 1 second before doing so. If it can't locate the element, it forfeits the action.
        <li><i>expSelect()</i></li>
		This function selects the first post in the explore page and opens it in pop-up mode. It waits 2 seconds before doing so.
        <li><i>topSelect()</i></li>
		This function selects the first post in the top posts section of any tag page and opens it in pop-up mode. It waits 2 seconds before doing so.
        <li><i>recSelect()</i></li>
		This function selects the first post in the recent posts section of any tag page and opens it in pop-up mode. It waits 2 seconds before doing so.
        <li><i>next()</i></li>
		This function clicks the next button next to a pop-up post. It waits 1 second before doing so. It returns 0 if it is able to find and click the button, otherwise it returns 1 and forfeits the action.
        <li><i>prev()</i></li>
		This function clicks the previous button next to a pop-up post. It waits 1 second before doing so. It returns 0 if it is able to find and click the button, otherwise it returns 1 and forfeits the action.
        <li><i>close()</i></li>
		This function close the previous of a pop-up post. It waits 1 second before doing so. If it can't locate the closing button, it forfeits the action.
        <li><i>scroll(dir)</i></li>
		This function scrolls instagram. It takes one parameter: dir, if the user wants to go to the top, then they must mention 'top' as the value of the dir parameter. Otherwise the function simply scrolls 400 pixels downwards. It waits 1 second before doing so.
        <li><i>postCount()</i></li>
		This function returns the number of posts that an account has. It waits 1 second before doing so.
        <li><i>follow()</i></li>
		This function presses the follow button in a profile. It waits 1 second before doing so. If it can't interact with the element, it forfeits the action.
        <li><i>unfollow()</i></li>
		This function presses the unfollow button in a pop-up prompt for the same. It can also cancel follow requests by withdrawing the request. It waits 1 second before diong so. If it can't interact with the element, it forfeits the action.
        <li><i>sugFollow(n)</i></li>
		This function follows accounts in the suggestions page. It takes one parameter n: where the input 'fol' makes the function follow accounts in the suggestions page itself. Otherwise it goes into each account seperately and here n acts as the index of the account in the suggestions page. It waits 1 second before doing so.
        <li><i>private()</i></li>
		This function returns 0 if an account is private or if a follow request has already been made and 1 if not. It waits 1 second before doing so. If it can't extract this information, it forfeits the action.
        <li><i>followingCount()</i></li>
		This function returns the number of accounts that any account is following. It waits 1 second before doing so.
        <li><i>followerCount()</i></li>
		This function returns the number of accounts that follow any account. It waits 1 second before doing so.
        <li><i>profFollowing()</i></li>
		This function opens the following pop-up menu of any account. It waits 1 second before doing so.
        <li><i>profUnfollow()</i></li>
		This function unfollows accounts in user's following page. It waits atleast 3 seconds before doing so.
        <li><i>postToProf()</i></li>
		This function goes to the account of the owner of any post open in pop-up mode. It waits 1 second before doing so.
        <li><i>topAccounts(num)</i></li>
		This function goes to instagram's top accounts section and selects the top profiles sequentially. It takes one parameter: num, this reflects the index of the profiles in the list that are to be interacted with. It waits for 1 second before doing so.
	</ul>
</details>
