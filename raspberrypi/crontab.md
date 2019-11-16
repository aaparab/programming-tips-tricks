## Crontab on Raspberry Pi:
---

To start crontab:
```
crontab -e
```

I'm currently running the following:
- Every Saturday (trailing `6`) at 3:00AM (leading `0 3`), update and upgrade the package list. 

```
0 3 * * 6 sudo apt-get update -y && sudo apt-get upgrade -y && sudo reboot now
```

- Every Sunday at 3:00 AM, upgrades pihole and the blocklists. 

```
0 3 * * 0 pihole -up && pihole -g
```
