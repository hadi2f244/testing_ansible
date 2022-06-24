import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_is_installed(host):
    docker = host.package("nginx")
    assert docker.is_installed

def test_docker_running_and_enabled(host):
    docker = host.service("nginx")
    assert docker.is_running
    assert docker.is_enabled

def test_nginx_responding(host):
    nginx_webserver = host.addr("127.0.0.1").port('80')
    assert nginx_webserver.is_reachable
