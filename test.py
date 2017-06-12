import Reddit

def main():
	file = open('subs', 'r')
	subs = file.read().split()
	print(subs)

	for sub in subs:
		subreddit = Reddit.getSubreddit(sub)
		print(subreddit.subscribers)
		posts = Reddit.getTopPosts(subreddit)
		filtered = Reddit.filter(posts, subreddit)

		for p in filtered:
			# prints tostring
			print(p.toString())

