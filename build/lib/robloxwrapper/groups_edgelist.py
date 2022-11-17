from .get_groups import groups
import time

def group_edgelist(id):
    groups_instance = groups(id)
    resp_allies = groups_instance.allies()
    ally_list = resp_allies['relatedGroups']
    ally_net = []
    new_ids = []
    for i in ally_list:
        new_ids.append(i['id'])
        ally_net.append([id, i['id']])
    for i in new_ids:
        try:
            new_groups_instance = groups(i)

            new_resp_allies = new_groups_instance.allies()
            #print(i)
            new_outer_list = new_resp_allies['relatedGroups']
            for j in new_outer_list:
                ally_net.append([i, j['id']])
        except:
             time.sleep(60)

    resp_enemies = groups_instance.enemies()
    enemy_list = resp_enemies['relatedGroups']
    enemy_net = []
    enemy_ids = []
    for i in enemy_list:
        enemy_ids.append(i['id'])
        enemy_net.append([id, i['id']])
    for i in enemy_ids:
        try:
            new_groups_instance = groups(i)

            new_resp_enemies = new_groups_instance.enemies()
            #print(i)
            new_outer_list = new_resp_enemies['relatedGroups']
            for j in new_outer_list:
                enemy_net.append([i, j['id']])
        except:
             time.sleep(60)
    d = dict()
    d['allies'] = ally_net
    d['enemies'] = enemy_net
    return d
