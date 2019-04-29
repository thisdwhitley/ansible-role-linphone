import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These tests are VERY specific to what's in molecule/default/playbook.yml
#  Currently my playbook creates these users:
#   test_usr1: no extra config specified so no tests here
#   test_usr2: irc_nick, servers, and channels specified
#   test_usr3: network_name, and servers specified
@pytest.mark.parametrize('file, content', [
    ("/home/test_usr2/.var/app/io.github.Hexchat/config/hexchat/hexchat.conf", "testUser2"),
    ("/home/test_usr2/.var/app/io.github.Hexchat/config/hexchat/servlist.conf", "6667"),
    ("/home/test_usr2/.var/app/io.github.Hexchat/config/hexchat/servlist.conf", "noob"),
    ("/home/test_usr3/.var/app/io.github.Hexchat/config/hexchat/servlist.conf", "ZNC"),
    ("/home/test_usr3/.var/app/io.github.Hexchat/config/hexchat/servlist.conf", "6667"),
])
def test_contents(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
