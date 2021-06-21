# AutoInsta
A side project, to simply help myself learn more about browser automation. The documentation is absolutely premature, just like the project itself. I will modify it once I'm happy with my progress at this.

## Actions
<ul>
	<!-- <li><b></b></li> -->
	<li><b>homLike(n)</b></li>
	This function likes posts in the home/feed section of Instagram. It takes one parameter: n, this is the number of posts that the function will like before scrolling back up top. The function waits for 4 seconds between each like, to make the activity seem more natural.
	<li><b>homDislike(n)</b></li>
	This function dislikes posts in the home/feed section of Instagram. It takes one parameter: n. The function waits for 4 seconds between each dislike.
	<li><b>postLike</b></li>
	This function likes pop-up posts. It waits 1 second before doing so to let the elements load properly.
	<li><b>postDislike</b></li>
	This function dislikes pop-up posts. It waits 1 second before doing so.
	<li><b>comment(text)</b></li>
	This function comments on pop-up posts. It waits 2 seconds before doing so. In case it cannot locate the commenting interface.
