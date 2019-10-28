## Random git-related notes
---

#### Turn off LF/CRLF warning (see [here](https://stackoverflow.com/a/14640908))

```
git config --global core.safecrlf false
```

#### Maintain multiple repositories from same laptop

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
