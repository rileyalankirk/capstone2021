Vagrant.configure("2") do |config|

    config.vm.define "database" do |database|
        database.vm.box = "ubuntu/trusty64"
        database.vm.hostname = "database"
        database.vm.network "private_network", ip:"20.0.0.20"

        database.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y redis-server

            # Start service that runs redis
            sudo systemctl start redis
        SCRIPT
    end

    config.vm.define "workserver" do |workserver|
        workserver.vm.box = "ubuntu/trusty64"
        workserver.vm.hostname = "workserver"
        workserver.vm.network "private_network", ip:"20.0.0.40"
        # Add "database" to /etc/hosts, which allows the workserver
        # to connect to the name database by name
        workserver.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"

        workserver.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server
            pip3 install venv
            git clone https://github.com/cs334s21/capstone2021
            cd capstone2021
            python3 -m venv .venv
            source .venv/bin/activate
            pip3 install -e .

            # Start workserver service
            sudo cp scripts/workserver.service /etc/systemd/system
            sudo chmod +x scripts/workserver.sh
            sudo systemctl start workserver
        SCRIPT
    end

    config.vm.define "client" do |client|
        client.vm.box = "ubuntu/trusty64"
        client.vm.hostname = "client"
        client.vm.network "private_network", ip:"20.0.0.60"
        # Add "workserver" to /etc/hosts, which allows the client
        # to connect to the name workserver by name
        client.vm.provision "shell", inline:"sed -i '$ a 20.0.0.40 workserver' /etc/hosts"

        client.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server
            pip3 install venv
            git clone https://github.com/cs334s21/capstone2021
            cd capstone2021
            python3 -m venv .venv
            source .venv/bin/activate
            pip3 install -e .

            # Start client service
            sudo cp scripts/client.service /etc/systemd/system
            sudo chmod +x scripts/client.sh
            sudo systemctl start client
        SCRIPT
    end

    config.vm.define "workgen" do |workgen|
        workgen.vm.box = "ubuntu/trusty64"
        workgen.vm.hostname = "workgen"
        workgen.vm.network "private_network", ip:"20.0.0.80"
        # Add "database" to /etc/hosts, which allows the workgen
        # to connect to the name database by name
        workgen.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"

        workgen.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server
            pip3 install venv
            git clone https://github.com/cs334s21/capstone2021
            cd capstone2021
            python3 -m venv .venv
            source .venv/bin/activate
            pip3 install -e .

            # Start workgen service
            sudo cp scripts/workgen.service /etc/systemd/system
            sudo chmod +x scripts/workgen.sh
            sudo systemctl start workgen
        SCRIPT
    end

    config.vm.define "dashboard" do |dashboard|
        dashboard.vm.box = "ubuntu/trusty64"
        dashboard.vm.hostname = "dashboard"
        dashboard.vm.network "private_network", ip:"20.0.0.100"
        # Add "database" to /etc/hosts, which allows the dashboard
        # to connect to the name database by name
        dashboard.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"

        dashboard.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server
            pip3 install venv
            git clone https://github.com/cs334s21/capstone2021
            cd capstone2021
            python3 -m venv .venv
            source .venv/bin/activate
            pip3 install -e .
            
            # Start dashboard service
            sudo cp scripts/dashboard.service /etc/systemd/system
            sudo chmod +x scripts/dashboard.sh
            sudo systemctl start dashboard
        SCRIPT
    end
end
