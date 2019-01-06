import os


def install_function():
    os.system('sudo yum install -y tcpdump')
    os.system('sudo yum -y update')
    os.system('sudo yum install -y net-tools')
    os.system('sudo yum install -y ifconfig')
    os.system('sudo yum install -y git')
    os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')
    os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
    os.system('sudo yum install -y docker-ce')
    # The following will install as root for the time bieng
    os.system('sudo usermod -aG docker $(whoami)')
    os.system('sudo systemctl enable docker.service')
    os.system('sudo systemctl start docker.service')
    os.system('sudo yum install -y epel-release')
    os.system('sudo yum install -y python-pip')
    os.system('sudo pip install docker-compose')
    os.system('sudo yum upgrade python*')
    try:
        os.mkdir('/docker')
    except OSError:
        print('/docker folder already exists!')
    os.system('sudo git pull https://github.com/ziwoz/BKP_SRV.git')
    os.system('cd BKP_SRV')
    os.system('sudo docker-compose -f /docker/BKP_SRV/docker-compose.yml build')
    os.system('sudo docker-compose -f /docker/BKP_SRV/docker-compose.yml up')


install_function()
