- Date : 2017-09-05
- Tags : #sysadmin #ansible

## Ansible playbook : skip to task

You can skip to a task by its name by adding parameter `--start-at`

```bash
$ ansible-playbook playbook.yml --start-at="[your task name]"
```

