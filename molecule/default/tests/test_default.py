import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

TEST_USER = "testuser"
THIS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def test_dconf_contents(host):
    """ Ensure that dconf output is as expected for our testuser """
    dconf_expected = open(os.path.join(THIS_DIRECTORY, 'dconf_expected')
                          ).read()
    with host.sudo(TEST_USER):
        dconf_contents = host.check_output("dconf dump /")

    assert dconf_contents == dconf_expected.rstrip()


@pytest.mark.parametrize("extension", [
                        "drop-down-terminal@gs-extensions.zzrough.org"])
def test_extensions_exist(host, extension):
    """ Ensure extensions got downloaded and enabled """

    default_extension_path = ".local/share/gnome-shell/extensions/"
    assert host.file('/home/{}/{}/{}'.format(
                                            TEST_USER,
                                            default_extension_path,
                                            extension))
    with host.sudo(TEST_USER):
        dconf_contents = host.check_output("dconf dump /org/gnome/shell/")

    assert extension in dconf_contents
