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
    try:
        os.mkdir('/docker/BKP_SRV')
    except OSError:
        print('/BKP_SRV folder already exists!')
    try:
        os.mkdir('/var/lib/persis')
    except OSError:
        print('/DB folder already exists!')
    os.system('sudo chmod -R 777 /var/lib/persis')
    os.system('sudo chmod 777 -R /var/lib/persis')
    
    # clone and install hynsyt from a specific commit ( tested production version )
    os.system('sudo git clone -n https://github.com/ziwoz/BKP_SRV.git /docker/BKP_SRV/')
    os.system('(cd /docker/BKP_SRV && sudo git checkout cd7fd9d2112b0e4433189f8e764eec97321c6502)')

    os.system('sudo docker-compose -f /docker/BKP_SRV/docker-compose.yml build')
    os.system('sudo docker-compose -f /docker/BKP_SRV/docker-compose.yml up')
    # https://coderwall.com/p/xyuoza/git-cloning-specific-commits # add the clone to the specific version here


install_function()
