from fabric.api import run, env, cd
from fabric.api import local
from fabric.colors import green, yellow
from fabric.contrib import files
from fabric.context_managers import prefix

env.hosts = ['54.199.246.223']
env.user = 'ubuntu'
env_base_path = '$HOME/.virtualenvs'
env_name = 'bgradar'
# app_path = '$HOME/BeautyGirlRadar'
app_path = '/var/www/BeautyGirlRadar'


def first_install():
    print(green("First Install Started..."))
    run('curl -O http://python-distribute.org/distribute_setup.py')
    run('sudo python distribute_setup.py')
    run('sudo easy_install pip')
    run('sudo pip install virtualenv')
    run('sudo pip install virtualenvwrapper')

    if not files.exists(env_base_path):
        run('mkdir $WORKON_HOME')

    with prefix('WORKON_HOME=' + env_base_path):
        run('echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc')
        run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc')
        run('echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bashrc')
        run('source ~/.bashrc')

    print(green("First Install End..."))


def apt_get_install():
    print(green("apt-get Install Started..."))
    run('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
    run("echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list")
    run('sudo add-apt-repository ppa:nginx/stable')
    run('sudo apt-get update')
    run('sudo apt-get install nginx')
    run('sudo apt-get install mongodb-org')
    run('sudo apt-get install git')
    run('sudo apt-get install python-dev')
    run('sudo aptitude install build-essential python-dev libjpeg-dev zlib1g-dev libfreetype6-dev')
    print(green("apt-get Install end..."))


def create_env(env_name):
    print(green("Create Started..."))

    with prefix('WORKON_HOME=' + env_base_path):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            if files.exists(env_base_path + '/' + env_name):
                run('rmvirtualenv ' + env_name)

            run('mkvirtualenv ' + env_name)

            with prefix('workon ' + env_name):
                with cd(app_path):
                    run('pip install -r pip-requires.txt')

    print(green("Create End..."))


def deploy():
    print(green("Deploy Started..."))
    # first_install()
    # apt_get_install()

    # if files.exists(app_path):
    #     run('rm -rf ' + app_path)

    with cd('/var/www/BeautyGirlRadar'):
        # run('sudo git clone https://github.com/wesgt/BeautyGirlRadar.git')
        run('sudo git pull')
    # run('git clone git@github.com:wesgt/BeautyGirlRadar.git')

    # create_env(env_name)
    print(green("Deploy End..."))


def chmod():
    # permission
    print(green("chmod Started..."))
    # run('sudo addgroup ubuntu')
    run('sudo adduser $USER ubuntu')
    run('sudo chown -R root:ubuntu /var/www')
    run('sudo find /var/www -type f -exec chmod 664 {} \;')
    run('sudo find /var/www -type d -exec chmod 775 {} \;')
    run('sudo find /var/www -type d -exec chmod g+s {} \;')

    print(green("chmod end..."))


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