This project contains codes for a workflow automation engine.

The library used is Celery for creating asynchronous tasks. And the broker service for queuing and Backend result is redis server.
Tasks can be run one after another using 'chain' and result passed onto the next task with 'signature', or tasks run parallel (at the same time time) using 'group'.

An example can be found in the automate.py file.

Thank you.
