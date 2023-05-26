import lodepy
from lodepy.git.status import Status

gr1 : lodepy.GroupReturn[int] = lodepy.GroupReturn({
  'n1': lodepy.NodeReturn(lodepy.Node('n1', '111'), 3),
})

res = gr1.execute_task(Status)

print(res.values['n1'])

#less_than_5.add_node()

less_than = gr1 < gr2


x = lodepy.import_groups_txt('test_group_text.txt')

print(x['group1'].nodes)