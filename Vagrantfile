Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.network "public_network", ip: "172.20.61.101"
    config.vm.synced_folder "./application", "/home/vagrant/application"
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 2

    end
    
        
    config.vm.provision "shell", inline: <<-SHELL
       
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip mysql-server redis-server python3-flask
        pip3 install redis pymysql
        pip install mysql-connector-python


        sudo sed -i "s/^bind-address/#bind-address/" /etc/mysql/mysql.conf.d/mysqld.cnf
        sudo echo "bind-address = 0.0.0.0" >> /etc/mysql/mysql.conf.d/mysqld.cnf
        
        sudo mysql -e "ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY '1234';"
        sudo service mysql restart
        
        mysql -u root -p1234 -e "CREATE DATABASE test"
        mysql -u root -p1234 -e "CREATE TABLE test.messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message VARCHAR(255)
        );"

        mysql -u root -p1234 -e "CREATE USER 'grafana'@'172.20.61.32';"
        mysql -u root -p1234 -e "CREATE USER 'app'@'localhost';"
        mysql -u root -p1234 -e "GRANT ALL PRIVILEGES ON test.* TO 'app'@'localhost';"
        mysql -u root -p1234 -e "GRANT SELECT ON test.* TO 'grafana'@'172.20.61.32';"
        mysql -u root -p1234 -e "FLUSH PRIVILEGES"
        
    SHELL


    config.vm.provision "shell", inline: <<-SHELL
        cd /home/vagrant/application
        flask run --host=0.0.0.0 --port=5000

    SHELL
end