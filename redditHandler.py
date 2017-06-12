import Reddit

def getHeadlines():
	sent_file = open('sent', 'r')
	subs = open('subs', 'r').read().split()

	sent = sent_file.read().split()
	sent_file.close()

	sent_file = open('sent', 'w')

	headlines = []

	for sub in subs:
		subreddit = Reddit.getSubreddit(sub)
		posts = Reddit.getTopPosts(subreddit)
		filtered = Reddit.filter(posts, subreddit)
		for p in filtered:
				if p.getId() not in sent:
					headlines.append(p.toString())
					print(p.toString())
					sent_file.write(" " + p.getId())

		sent_file.close()

if __name__ == '__main__':
	getHeadlines()
