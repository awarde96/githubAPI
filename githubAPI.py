from github import Github
import getpass

#g = Github("user", "password")
username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username,pw)

for repo in g.get_user().get_repos():
    print repo.name
    numberOfCommits = 0
    for commit in repo.get_commits():
        #print commit
        numberOfCommits += 1
    print "Number of Commits: " + repr(numberOfCommits)
    for collaborators in repo.get_collaborators():
        print collaborators
    for languages in repo.get_languages():
       print languages
    for branch in repo.get_branches():
        print branch
        print ""
    print repo.get_stats_contributors()


email = raw_input("Email:")
print g.legacy_search_user_by_email(email)

print g.get_last_api_status_message()
