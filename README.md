# AutoInsta
A side project, to simply help myself learn more about browser automation. The documentation is absolutely premature, just like the project itself. I will modify it once I'm happy with my progress at this.

## Actions
The action class contains functions that interact with the interface of the website. Below is a list of all the functions in this class and a description of what each of them does.
<ul>
	<!-- <li><i></i></li> -->
	<li><i>homLike(n)</i></li>
	This function likes posts in the home/feed section of Instagram. It takes one parameter: n, this is the number of posts that the function will like before scrolling back up top. It waits for 4 seconds between each like, to make the activity seem more natural.
	<li><i>homDislike(n)</i></li>
	This function dislikes posts in the home/feed section of Instagram. It takes one parameter: n. It waits for 4 seconds between each dislike.
	<li><i>postLike()</i></li>
	This function likes pop-up posts. It waits 1 second before doing so to let the elements load properly.
	<li><i>postDislike()</i></li>
	This function dislikes pop-up posts. It waits 1 second before doing so.
	<li><i>comment(text)</i></li>
	This function comments on pop-up posts. It takes a parameter: text, this is the text that is commented on a post. It waits 2 seconds before doing so. If it can't locate the commenting interface, it forfeits the action.
	<li><i>postSelect()</i></li>
	This function selects posts and presents them in a pop-up format from profile/explore/tag pages to help other functions interact with the post. It waits 1 second before doing so. If it can't locate the post, it forfeits the action.
	<li><i>next()</i></li>
	This function clicks the next button next to a pop-up post. It waits 1 second before doing so. It returns 0 if it is able to find and click the button, otherwise it returns 1 and forfeits the action.
	<li><i>prev()</i></li>
	This function clicks the previous button next to a pop-up post. It waits 1 second before doing so. It returns 0 if it is able to find and click the button, otherwise it returns 1 and forfeits the action.
	<li><i>close()</i></li>
	This function close the previous of a pop-up post. It waits 1 second before doing so. If it can't locate the closing button, it forfeits the action.
	<li><i>scroll(dir)</i></li>
	This function scrolls instagram. It takes one parameter: dir, if the user wants to go to the top, then they must mention top as the value of the dir parameter. Otherwise the function simply scrolls 400 pixels downwards. It waits 1 second before doing so.
	<li><i>postCount()</i></li>
	This function returns the number of posts that an account has. It waits 1 second before doing so.
	<li><i>postSelect()</i></li>
	This function selects the first post in any account in the pop-up mode. It waits 1 second before doing so. If it can't locate the element, it forfeits the action.
	<li><i>follow()</i></li>
	This function presses the follow button in a profile. It waits 1 second before doing so. If it can't interact with the element, it forfeits the action.
	<li><i>private()</i></li>
	This function returns 0 if an account is private and 1 if not. It waits 1 second before doing so. If it can't extract this information, it forfeits the action
</ul>
