# -*- coding: utf-8 -*-

config = {
    'login'             :   '',       # Your VK login
    'password'          :   '',    # Your VK password
    'token'             :   '',       # Your VK token
    'group_id'          :   '',		# Group id Like -1XXXXXXXX without ''
    'count_last_posts'  :    3,	            # Count of last posts to be 				   | 10 posts
    'liked_last_posts'  :    True,			    # Procedure of Liked Last Count of Wall Posts. | True or False
    'liked_new_posts'   :    True,		        # Start deamon to liked new group post.        | True or False
    'cooldown_like'     :    0.5,               # Cooldown between liked last group posts in seconds. !Very low cooldown may cause captcha error
    'cooldown_check'    :    5                # Cooldown between check new posts from group in seconds.
}
