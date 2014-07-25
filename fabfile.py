from fabric.api import run, env
from fabric.api import local
from fabric.colors import green, yellow
from fabric.contrib import files
from fabric.context_managers import prefix

env.hosts = ['54.92.113.106']
env.user = 'ubuntu'
env_base_path = '$HOME/.virtualenvs'
env_name = 'ideal'


def first_install():
    print(green("First Install Started..."))
    run('curl -O http://python-distribute.org/distribute_setup.py')
    run('sudo python distribute_setup.py')
    run('sudo easy_install pip')
    run('sudo pip install virtualenv')
    run('sudo pip install virtualenvwrapper')

    if not files.exists(env_base_path):
        run('mkdir $WORKON_HOME')

    print(green("First Install End..."))


def apt_get_install():
    print(green("apt-get Install Started..."))
    # run('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
    # run("echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list")
    # run('sudo apt-get update')
    # run('sudo apt-get install mongodb-org')
    run('sudo apt-get install git')
    # run('sudo service mongod start')
    print(green("apt-get Install end..."))


def create_env():
    print(green("Create Started..."))

    with prefix('WORKON_HOME=' + env_base_path):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            if files.exists(env_base_path + env_name):
                run('rmvirtualenv ' + env_name)

            run('mkvirtualenv ' + env_name)

            with prefix('workon ' + env_name):
                run('pip list')
                # run('pip install -r requirements.txt')

    print(green("Create End..."))


def deploy():
    # first_install()
    apt_get_install()
    # create_env()


def is_local():
    local('ls')


def host_type():
    run('uname -s')


def hello(name="world"):
    print("Hello %s!" % name)


def filepath():
    remote_dir = '/opt/xxx'
    with cd(remote_dir):
        run("touch README")


def set_hosts():
    env.hosts = ['host1', 'host2']


def mytask():
    run('ls /var/www')