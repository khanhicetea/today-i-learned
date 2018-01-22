- Date : 2018-01-22
- Tags : #devops #ansible

## Ansible running host pattern

Ansible supports pattern to select and filter running hosts from all hosts. Here is some common pattern

- `*` : wildcard, standalone mean `all`
- `group1,group2` : run hosts belong to group1 or group2
- `*.web` : run hosts belongs to group matches pattern. Ex: `backend.web`, `frontend.web`
- `all:!abc` : run all hosts exclude hosts belongs to group `abc`

> Infrastructure by code ;)

