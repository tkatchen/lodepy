# lodepy
lodepy is a Multi-node fully python automation tool. It is agentless and executes tasks over SSH.

# The concept
In a nutshell, lodepy serves a pretty simple task: execute ssh commands on servers to set them up.

With this comes a variety of somewhat neccessary functionalities that lodepy implements:
* Execute the commands (obviously) within well defined "Groups" of "Nodes"
* Create a well defined logging system to stream and monitor task execution
* Provide a clean wrapper / execution model to seamlessly run operations and comparisons on multiple results.

# Using lodepy
In it's current state the main interaction is going to be with the [Group](https://github.com/tkatchen/lodepy/blob/main/src/lodepy/groups/group.py) class and its subclasses (namely the [GroupReturn](https://github.com/tkatchen/lodepy/blob/main/src/lodepy/groups/group_return.py)).

1) Definining a group is quickly done with the use of `Main.import_group_txt(file: str) -> Dict[str, Group]`
   1) This is going to be in the format of:
      ```
      [group1]

      node1, 1.1.1.1
      node2, 1.1.1.2

      [group2]

      node3, 1.1.1.1
      node4, 1.1.1.1

      [group_name]
      node_name, ssh_ip
      ```
   2) Note, already created groups can be found in the `Main.get_groups()`

2) Executing commands
   1) We can then execute a variety of Group commands. A series of these are listed as functions of Group.py.
   2) Some commands can be custom created. In this case you simply need to:
      1) Define the Task
      2) `<Group>.execute_task(<Task>(params))`

3) Using these resulting GroupReturn
   1) Filtering
      1) GroupReturns handle filtering in the such way:
          ```python
          group_return = GroupReturn()
          double_lt_5 = group_return * 2 < 5
          # double_lt_5 is going to be the GroupReturn filtered with only nodes doubled returning a value less than 5.
          ```
           1) Note, this also works with versioning. A command like git_version will be able to handle filtering such as `group_return > 1.0.*`
   2) Executing future commands
      1) GroupReturns are simply subclasses of a Group. They can exectue commands and function entirely similarly.
   3) Any operations available to the value class
      1) Group returns aim to be abtract enough that any of the commands it's value expects to handle, so can the GroupReturn


In total this is the entire functionality loop of lodepy. There is still more to cover (and to implement), but to expect: log handling / streaming results elsewhere, more configurability (error handling, execution tuning, etc.), a variety of builtin Tasks for common usecases and the ability to seamlessly create more Tasks (and recursively handle encapsuled tasks).

# Example

```python
with Script() as s:
    # Get new groups
    groups = s.import_group_txt('groups.txt')
    # or if we've imported before:
    groups = s.get_groups()

    # Get a specific group and execute a task
    group1 = groups['group1']
    res = group1.execute_task(GitVersion())

    # Filter result and update old versions
    old_versions = res < '1.0.0'
    old_versions.execute_task(APTGet('git', version='1.0.0'))
```