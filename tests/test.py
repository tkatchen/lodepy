import lodepy
from lodepy.core.version import Version
from lodepy.git.git_status import GitStatus
from lodepy.handling.log_manager import LogManager

gr1 : lodepy.GroupReturn[int] = lodepy.GroupReturn({
  'n1': lodepy.NodeReturn(lodepy.Node('n1', 'localhost'), 3, 0),
  'n2': lodepy.NodeReturn(lodepy.Node('n2', 'localhost'), 2, 0)
})

x = Version('1.0.1')

print(x == '1.0.0')

print(x == '1.0.*')

res = gr1.execute_task(GitStatus)

print(res.values['n1'])

#less_than_5.add_node()

#print(LogManager.get_logs())


x = lodepy.import_groups_txt('test_group_text.txt')

print(x['group1'].nodes)