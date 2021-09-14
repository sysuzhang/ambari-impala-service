import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core.base import Fail
from resource_management.core.exceptions import ComponentIsNotRunning
from subprocess import call


class ImpalaDaemon(Script):
    #Call setup.sh to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)

        cmd = 'yum -y install yum-utils && yum-config-manager --add-repo  ' \
              'http://repo.topdata.cloud/repos/cloudera/cloudera-cdh6.repo'

        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)


        cmd = 'yum -y install  impala-server impala-shell'
        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)

        self.configure(env)

    def configure(self, env):
        import params

        env.set_params(params)


    #Call start.sh to start the service
    def start(self, env):
        cmd = 'systemctl start impala-server'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    #Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'systemctl stop impala-server'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    #Called to get status of the service using the pidfile
    def status(self, env):
        cmd = 'systemctl status impala-server'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

if __name__ == "__main__":
    ImpalaDaemon().execute()
