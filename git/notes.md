## Random git-related notes
---

- ### The awesome `git stash`:

	**Issue:** I made changes to local repository and collaborator pushed their changes in remote. 
	How do I `git pull` but making sure my local changes are not lost? 

	**Solution:** (Taken from [this](https://stackoverflow.com/a/19216491) answer)
	```
	git stash
	git pull origin master
	git stash pop
	```
	
- ### `master` is offensive:
	**Issue:** Github has renamed the default branch from `master` to `main` whereas a newly created repository has `master` as the default branch. This causes problems with `git pull`. To solve this, let us rename our local `master` branch to `main`. 
	
	**Solution:** (Taken from [here](https://hackernoon.com/how-to-rename-your-git-repositories-from-master-to-main-6i1u3wsu))
	```
	git branch -m master main
	```

- ### Ignored added files after changing `.gitignore`

	**Issue:** How to refresh the file index after making changes to `.gitignore`? 
	
	**Solution:** Found [here](https://stackoverflow.com/questions/1274057/how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore)
	
	```
	git rm -r --cached .
	git add --all
	git commit -m "Remove ignored files."
	```
	(or)
	```
	git update-index --assume-unchanged .
	```

- ### Switch between `vim` and `VS Code` as commit editors:

	```
	git config --global core.editor "code --wait"
	git config --global core-editor "vi"
	```
	**Reference** [here](https://stackoverflow.com/a/52196507)

- ### Fast-forward a branch to head:

	**Issue:** I made changes to local whereas someone else made changes to remote. When I do `git status`, I get:
	> Your branch is behind 'origin/master' by 2 commits, and can be fast-forwarded.

	**Solution:** (Taken from [here](https://stackoverflow.com/a/9512565))
	```git merge --ff-only origin/master```

- ### Turn off LF/CRLF warning (see [here](https://stackoverflow.com/a/14640908))

	```
	git config --global core.safecrlf false
	```

- ### Maintain multiple repositories from same laptop

	**Problem**: Suppose I have two github accounts and would like to work with both using the same local machine. How to use different encryption keys for them?

	**Solution**: Found [here](https://stackoverflow.com/a/21161120). Create two keys and add them to respective github accounts. In order to decide which key (`~/.ssh/id_rsa_key1/2`), change the config files under `~/.ssh/config` and `./.git/config` files appropriately, namely:

	1. 
	```
	cat ~/.ssh/config
	Host github-1
		HostName github.com
		User git
		IdentityFile ~/.ssh/id_rsa_key1
	Host github-2
		HostName github.com
		User git
		IdentityFile ~/.ssh/id_rsa_key2
	```

	2. 
	```
	cat dir1/.git/config
	git@github-1:<user1>/<repo1>.git
	```

	```
	cat dir2/.git/config
	git@github-2:<user2>/<repo2>.git
	```
	
- ### Addendum to above: 

	- Global config is stored at `~/.gitconfig` and can be accessed using `git config --list`. 
	- To update name and email for a specific local repository, use 
	```
	git config user.name "Foo Name"
	git config user.email "foo@email.com"
	```
