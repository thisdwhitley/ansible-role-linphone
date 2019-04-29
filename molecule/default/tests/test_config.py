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
    ("/home/test_usr1/.var/app/com.belledonnecommunications.linphone/config/linphone/linphonerc", "test_usr1"),
    ("/home/test_usr1/.var/app/com.belledonnecommunications.linphone/config/linphone/linphonerc", "1234567890"),
    ("/home/test_usr1/.var/app/com.belledonnecommunications.linphone/config/linphone/linphonerc", "S3cr3t"),
    ("/home/test_usr1/.var/app/com.belledonnecommunications.linphone/config/linphone/linphonerc", "sip.network.com"),
    ("/home/test_usr1/.var/app/com.belledonnecommunications.linphone/config/linphone/linphonerc", "0123456789"),
])
def test_contents(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
