#!/usr/bin/python3
#!/usr/bin/env python3
"""
This module contains a Fabric script for deploying a web_static archive to web servers
"""
from fabric.api import env, run, put
from os import path
from datetime import datetime
# Set the user and IP address for accessing the web servers
env.user = 'ubuntu'
env.hosts = ['54.242.117.7', '54.226.19.77']


def do_pack():
    now = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(archive_path))
    if path.exists(archive_path):
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    filename = archive_path.split("/")[-1]
    folder_name = "/data/web_static/releases/" + filename[:-4]
    run("mkdir -p {}".format(folder_name))
    run("tar -xzf /tmp/{} -C {}".format(filename, folder_name))
    run("rm /tmp/{}".format(filename))
    run("rm -f /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(folder_name))

    return True

def deploy():
    """
    Deploy web_static archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

