from .get_friends import friends
import time

def friend_edgelist(id):
    friends_instance = friends(id)
    response = friends_instance.info()
    outer_list = response['data']
    l = []
    new_ids = []
    for i in outer_list:
        new_ids.append(i['id'])
        l.append([id, i['id']])
    for i in new_ids:
        try:
            new_friends_instance = friends(i)

            new_response = new_friends_instance.info()
            print(i)
            new_outer_list = new_response['data']
            for j in new_outer_list:
                l.append([i, j['id']])
        except:
             time.sleep(60)

    return l
