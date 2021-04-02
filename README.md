# PyRoblox
Python wrapper for the Roblox API.

## Notes
Roblox's API does not require a developer account (or an account at all). Its endpoints are exposed to the public, and its rate limits are generous. Please use common sense when using this so we can continue researching Roblox data in such an open capacity.

## Installation

```
git clone https://github.com/CTEC-MIIS/PyRoblox
cd PyRoblox
pip install .
```

## Usage
### Master Function
This library provides a function that will generate a handful of csvs given a group ID:
* Ally edgelists 
* Enemy edgelists
* Group info
* Member-group edgelists for all groups in the Ally and Enemy lists
* User info for all members
* Member-Favorited Asset edgelist for all users
* Asset info for all favorited assets

This function needs a Roblox Security cookie. When logged into a Roblox account, go to developer tools and find the ROBLOSECURITY cookie. Format like this: `{".ROBLOSECURITY": "alphanumericstring"}`

```build_dataframes(group_id, {".ROBLOSECURITY": "alphanumericstring"})```

### User Functions

To get user info, including created date, username, and description, use the following:

```
from PyRoblox import robloxwrapper as rw
rw.user_info(user_id)
```

### Group Functions

To get group info, use the following:

```
from PyRoblox import robloxwrapper as rw
rw.group_info(group_id)
```

The `group_edgelist` function also returns full edgelists of a group's ally and enemy affiliations. 

```rw.group_edgelist(group_id)```

This function returns a dictionary with keys `allies` and `enemies`, where the values are list of lists representing the edgelists of the two-step network from the initial group ID.

### Friend Functions

The `friend_edgelist` function returns a list of lists that represents the edgelist of the two-step network from the initial user ID. 

```
from PyRoblox import robloxwrapper as rw
rw.friend_edgelist(user_id)
```
