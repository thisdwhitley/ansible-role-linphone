import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_linphone_installed(host):
    # I used to check with hexchat.is_installed, that doesn't work with flatpak
    assert host.check_output('flatpak info com.belledonnecommunications.linphone')
