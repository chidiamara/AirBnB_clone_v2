#!/usr/bin/python3
"""
a fabric script that distributes an archive to web servers
"""

from fabric.operations import local, put, run
from fabric.api import *
from datetime import datetime as dt

env.hosts = ["18.209.224.9", "34.232.72.45"]


def do_pack():
    """ generates a .tgz archive """
    name = "versions/web_static_" + str(dt.now().year)
    name += str(dt.now().month) + str(dt.now().day) + str(dt.now().hour)
    name += str(dt.now().minute) + str(dt.now().second) + ".tgz"
    result = local("mkdir -p versions; tar -cvzf \"%s\" web_static" % name)
    if result.failed:
        return None
    else:
        return Name


def do_deploy(archive_path):
    """ this function uploads the archive to servers """
    destination = "/tmp/" + archive_path.split("/")[-1]
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    filename = archive_path.split("/")[-1]
    f = filename.split(".")[0]
    directory = "/data/web_static/releases/" + f
    run_res = run("mkdir -p \"%s\"" % directory)
    if run_res.failed:
        return False
    run_res = run("tar -xzf %s -C %s" % (destination, directory))
    if run_res.failed:
        return False
    run_res = run("rm %s" % destination)
    if run_res:
        return False
    web = directory + "/web_static/*"
    run_res = run("mv %s %s" % (web, directory))
    if run_res.failed:
        return False
    web = web[0:-2]
    run_res = run("rm -rf %s" % web)
    if run_res.failed:
        return False
    run_res = run("rm -rf /data/web_static/current")
    if run_res.failed:
        return False
    run_res = run("ln -s %s /data/web_static/current" % directory)
    if run_res.failed:
        return False
    return True
