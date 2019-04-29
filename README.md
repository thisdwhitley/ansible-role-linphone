# Ansible Role: linphone

This is an Ansible role to install and potentially configure the
[linphone](https://www.linphone.org/) SIP phone.

I prefer to pass the variables "into" the role from the playbook versus by
including variable files.  This is because I hope to make the role usable by
other projects/roles.  I don't know if this logic makes sense or not, but I am
essentially attempting to remove the variables from the role itself.

This is widely available in repositories, but as of April 2019 I have shifted to
preferring flatpaks to repository/package installs.

## Overview

At a very high level, this role will:

* install the linphone flatpak
* [*optional*] if a username is provided, it will template out a generic
  `~/.linphonerc` file (using what I hope are sane defaults for any missing
  variables)

The testing of this role is very specific to the role I've set up in molecule,
but I think I'm ok with that.

## Important Notes

* This role will install the latest version of the flatpak

## Requirements

Any package or additional repository requirements will be addressed in the role.

## Role Variables

All of these variables should be considered **optional** however, be aware that
sanity checking is minimal (if at all):

* `users` *ideally you could configure linphone differently per user, and this
          nested list of users allows for that*
  * `username`
    * this is the username on the OS **NOTE: this role will not create the
      user!**
  * `number`
    * obviously a phone needs a number; if none is passed, **1111111111** is
      inserted in the hopes to catch your eye the first time you use `linphone`
  * `password`
    * this is in plain text so adhere to all general guidelines and cautions; if
      none is passed, the default will be an empty string
  * `realm`
    * this is the SIP realm; if none is passed, **sip.example.com** will be used
  * `friends`
    * this is a ***list*** consisting of:
      * `name`
        * the name associated with a number
      * `number`
        * the saved number (use 10 digits, a "1" will be prepended to it)

## Example Playbook

Playbook with configuration options specified:

```yaml
- hosts: localhost
  connection: local
  roles:
    - role: linphone
      users:
        - username: user1
          number: 1234567890
          password: S3cr3t
          realm: sip.network.com
          friends:
            - name: "My Friend"
              number: 0123456789
            - name: "Another Friend"
              number: 9012345678
```

## Inclusion

I envision this role being included in a larger project through the use of a
`requirements.yml` file.  So here is an example of what you would need in your
file:

```yaml
# get the linphone role from gitlab
- src: https://github.com/thisdwhitley/ansible-role-linphone.git
  scm: git
  name: linphone
```

Have the above in a `requirements.yml` file for your project would then allow
you to "install" it (prior to use in some sort of setup script?) with:

```bash
ansible-galaxy install -p ./roles -r requirements.yml
```

## Testing

I am relying heavily on the work by Jeff Geerling in using molecule for testing
this role.  I have, however, modified the tests to make them specific to what I
am attempting to accomplish but this could still use some work.

Please review those files, but here is a list of OSes currently being tested 
(using geerlingguy's container images):

* centos7
* fedora27
* fedora28
* fedora29
* ubuntu18
* debian9

## To-do

* verify that I'm testing what I think I'm testing

## References

* [How I test Ansible configuration on 7 different OSes with Docker](https://www.jeffgeerling.com/blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker)

## License

All parts of this project are made available under the terms of the [MIT
License](LICENSE).