Tasks
=====

Tasks are the core functionality of lodepy.

Running a Task
--------------

Running a Task is as simple as:

.. code-block:: python

   Group.execute_task(Task(params))

This will execute the task on all of the nodes that are within the Group.
Furthermore, the return values can be captured by simply setting

.. code-block:: python

   group_return = Group.execute_task(Task(params))

On top of this, any pass/fail messages will be sent to the LogManager, and can be streamed anywhere youd like.

Git
=====

..automodule:: lodepy.git.git_status
  :members: