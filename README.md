# PyRoblox
Python wrapper for the Roblox API.

## Notes
Roblox's API does not require a developer account (or an account at all). Its endpoints are exposed to the public, and its rate limits are generous. Please use common sense when using this so we can continue researching Roblox data in such an open capacity.

## Installation

```git clone https://github.com/CTEC-MIIS/PyRoblox```

```cd PyRoblox```

```pip install .```

## Usage
### User Functions

To get user info, including created date, username, and description, use the following:

```from PyRoblox import robloxwrapper as rw```

```rw.user_info(user_id)```

### Group Functions

To get group info, use the following:

```from PyRoblox import robloxwrapper as rw```

```rw.group_info(group_id)```

The `group_edgelist` function also returns full edgelists of a group's ally and enemy affiliations. 

```rw.group_edgelist(group_id)```

This function returns a dictionary with keys `allies` and `enemies`, where the values are list of lists representing the edgelists of the two-step network from the initial group ID.

### Friend Functions

The `friend_edgelist` function returns a list of lists that represents the edgelist of the two-step network from the initial user ID. 

```from PyRoblox import robloxwrapper as rw```

```rw.friend_edgelist(user_id)```
