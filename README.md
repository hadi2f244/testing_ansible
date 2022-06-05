# Testing Ansible
Testing Ansible code example.
Follow these medium posts:

- Part 1 - Test Environment Automation
- Part 2 - Writing Tests
- Part 3 - Writing Tests (I need more!)
- Part 4 - **ansible-test** command


# Requirements
+ Ansible (*Tested on `2.12.2`*)
+ Docker (*Tested on `20.10.10`*)
+ Vagrant (*Tested on `2.2.6`*)
+ Molecule (*Tested on  `3.5.2`*):

    `pip install 'molecule[docker]' ansible-lint molecule-vagrant`

# Test Scenario

1. `molecule create -s docker`
2. `molecule lint -s docker`
3. `molecule converge -s docker`
4. `molecule verify -s docker`
5. `molecule idempotence -s docker`
6. `molecule destroy -s docker`

OR use `molecule test -s docker` instead.
