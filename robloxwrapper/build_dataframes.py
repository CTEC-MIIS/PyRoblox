from .get_groups import groups
from .get_friends import friends
from .get_games import group_games, user_games
from .groups_edgelist import group_edgelist
from .friends_edgelist import friend_edgelist
import pandas as pd
import time

def build_dataframes(group_id, cookie):
    el = group_edgelist(group_id)
    allies = pd.DataFrame(el['allies'], columns =['From', 'To'])
    enemies = pd.DataFrame(el['enemies'], columns =['From', 'To'])
    group_ids = set(list(allies['To']) + list(allies['From']) + list(enemies["To"]) + list(enemies["From"]))
    print(group_ids)
    big_list = []
    print("Getting group info... length is: ", len(group_ids))
    for i in list(group_ids):
        while(True):
            print(i)
            # print(big_list)
            # print(groups(i).social_links())
            #print(groups(i).info().values())
            try:

                socials = groups(i).social_links(cookies = cookie)
                print(socials.keys())
                if 'data' in socials.keys():
                # print(socials)
                    socials = socials['data']
                    social_list = []
                    if len(socials) > 0:
                        for j in socials:
                            social_list.append(j)
                else:
                    social_list = []
                group_info = groups(i).info()
                print("errors" in group_info.keys())
                if "errors" in group_info.keys():
                    time.sleep(60)
                    group_info = groups(i).info()

                print(list(group_info.values()) + social_list)
                print(social_list)
                big_list.append(list(group_info.values()) + social_list)
            except:
                time.sleep(60)
                continue
            break
    group_info_df = pd.DataFrame(big_list, columns = ["id", "name", "description", "owner", "shout", "memberCount", "isBuildersClubOnly", "publicEntryAllowed", "isLocked", "social1", "social2"])
    group_info_df.to_csv("group_info_{}.csv".format(group_id))
    group_el = []
    print("Groups to collect: ", len(group_ids))
    for i in list(group_ids):
        friends_list = groups(group_id).user_list()
        for j in friends_list['data']:
            group_el.append([i, j['user']['userId']])
        cursor = friends_list['nextPageCursor']
        while cursor is not None:
            friends_list = groups(group_id).user_list(cursor=cursor)
            for j in friends_list['data']:
                group_el.append([i, j['user']['userId']])
            cursor = friends_list['nextPageCursor']
    group_membership_el = pd.DataFrame(group_el, columns = ['Group', 'User'])
    user_ids = set(list(group_membership_el['User']))
    big_list = []
    print("Getting user info... length is: ", len(user_ids))
    for i in list(user_ids):
        while True:
            try:
                big_list.append(list(friends(i).user_info().values()))
            except:
                time.sleep(60)
                continue
            break
    user_info_df = pd.DataFrame(big_list, columns = ["description", "created", "isBanned", "id", "name", "displayName"])
    favorites_el = []
    games_dict = {}
    favorites_l = []
    for i in user_ids:
        while(True):
            try:
                print(i)
                favorites_l = user_games(i).favorites_list()
                print(len(favorites_l['data']))
                if len(favorites_l['data']) > 0:
                    for j in favorites_l['data']:
                        favorites_el.append([i, j['id']])
                        if j['id'] not in games_dict.keys():
                            games_dict[j['id']] = [j['name'], j['description'], j['creator']['id'], j['created'], j['placeVisits']]
                    cursor = favorites_l['nextPageCursor']
                    favorites_l = favorites_l = user_games(i).favorites_list(cursor=cursor)
                    print(len(games_dict.keys()))
            except:
                print("sleeping...")
                time.sleep(60)
                continue
            break
    asset_el_df = pd.DataFrame(favorites_l, columns=["User", "FavoritedGame"])
    asset_info_df = pd.DataFrame.from_dict(games_dict, orient='index')


    allies.to_csv("allies_{}_edgelist.csv".format(group_id))
    enemies.to_csv("enemies_{}_edgelist.csv".format(group_id))
    group_membership_el.to_csv("membership_{}_edgelist.csv".format(group_id))
    user_info_df.to_csv("user_info_membership_{}.csv".format(group_id))
    group_info_df.to_csv("group_info_{}.csv".format(group_id))
    asset_el_df.to_csv("asset_el{}.csv".format(group_id))
    asset_info_df.to_csv("asset_info_{}.csv".format(group_id))
