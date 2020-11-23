# Linux tips:
---

## Passwordless SSH:
1. On the source machine, generate the ssh key by running `ssh-keygen`,
2. Two files are generated in the .ssh/ folder, `id_rsa` and `id_rsa.pub`,
3. Add the public key to the destination by `ssh-copy-id -i ~/.ssh/id_rsa.pub <remote-user>@<remote-host>`
4. From my Dell machine, I do: ssh-copy-id -i /c/Users/msabp/.ssh/id_rsa.pub csmrnd01
5. Reference: https://goo.gl/8vdzGE

### Addendum: Automatic Port-Forwarding
1. Add the following line to the particular hostname to enable automatic port forwarding:
```
LocalForward 8157 localhost:8765
```

### Force password input:
1. `ssh -o PubkeyAuthentication=no www.server.com`
