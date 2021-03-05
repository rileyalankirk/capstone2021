Vagrant.configure("2") do |config|

    config.vm.define "database" do |database|
        database.vm.box = "ubuntu/bionic64"
        database.vm.hostname = "database"
        database.vm.network "private_network", ip:"20.0.0.20"

        database.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y redis-server
        SCRIPT
        database.vm.provision "shell", run: "always", inline:<<-SCRIPT
            # Start service that runs redis
            sudo systemctl start redis
        SCRIPT
    end

    config.vm.define "workserver" do |workserver|
        workserver.vm.box = "ubuntu/bionic64"
        workserver.vm.hostname = "workserver"
        workserver.vm.network "private_network", ip:"20.0.0.40"
        # Add "database" to /etc/hosts, which allows the workserver
        # to connect to the name database by name
        workserver.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"
        workserver.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server python3-venv
            git clone https://github.com/rileyalankirk/capstone2021
            cd capstone2021
            sudo git checkout remotes/origin/automate
            sudo python3 -m venv .venv
            source .venv/bin/activate
            sudo pip3 install -e .

            # Copy service into system folder and make shell script executable
            sudo cp scripts/workserver.service /etc/systemd/system
            sudo chmod +x scripts/workserver.sh
        SCRIPT
        workserver.vm.provision "shell", run: "always", inline:<<-SCRIPT
            # Start workserver service
            sudo systemctl start workserver
        SCRIPT
    end

    config.vm.define "client" do |client|
        client.vm.box = "ubuntu/bionic64"
        client.vm.hostname = "client"
        client.vm.network "private_network", ip:"20.0.0.60"
        # Add "workserver" to /etc/hosts, which allows the client
        # to connect to the name workserver by name
        client.vm.provision "shell", inline:"sed -i '$ a 20.0.0.40 workserver' /etc/hosts"

        client.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server python3-venv
            git clone https://github.com/rileyalankirk/capstone2021
            cd capstone2021
            sudo git checkout remotes/origin/automate
            sudo python3 -m venv .venv
            source .venv/bin/activate
            sudo pip3 install -e .

            # Copy service into system folder and make shell script executable
            sudo cp scripts/client.service /etc/systemd/system
            sudo chmod +x scripts/client.sh
        SCRIPT
        client.vm.provision "shell", run: "always", inline:<<-SCRIPT
            # Start client service
            sudo systemctl start client
        SCRIPT
    end

    config.vm.define "workgen" do |workgen|
        workgen.vm.box = "ubuntu/bionic64"
        workgen.vm.hostname = "workgen"
        workgen.vm.network "private_network", ip:"20.0.0.80"
        # Add "database" to /etc/hosts, which allows the workgen
        # to connect to the name database by name
        workgen.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"

        workgen.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server python3-venv
            git clone https://github.com/rileyalankirk/capstone2021
            cd capstone2021
            sudo git checkout remotes/origin/automate
            sudo python3 -m venv .venv
            source .venv/bin/activate
            sudo pip3 install -e .

            # Copy service into system folder and make shell script executable
            sudo cp scripts/workgen.service /etc/systemd/system
            sudo chmod +x scripts/workgen.sh
        SCRIPT
        workgen.vm.provision "shell", run: "always", inline:<<-SCRIPT
            # Start workgen service
            sudo systemctl start workgen
        SCRIPT
    end

    config.vm.define "dashboard" do |dashboard|
        dashboard.vm.box = "ubuntu/bionic64"
        dashboard.vm.hostname = "dashboard"
        dashboard.vm.network "private_network", ip:"20.0.0.100"
        # Add "database" to /etc/hosts, which allows the dashboard
        # to connect to the name database by name
        dashboard.vm.provision "shell", inline:"sed -i '$ a 20.0.0.20 database' /etc/hosts"

        dashboard.vm.provision "shell", inline:<<-SCRIPT
            sudo apt-get update
            sudo apt-get install -y python3-pip git redis-server python3-venv
            git clone https://github.com/rileyalankirk/capstone2021
            cd capstone2021
            sudo git checkout remotes/origin/automate
            sudo python3 -m venv .venv
            source .venv/bin/activate
            sudo pip3 install -e .

            # Copy service into system folder and make shell script executable
            sudo cp scripts/dashboard.service /etc/systemd/system
            sudo chmod +x scripts/dashboard.sh
        SCRIPT
        dashboard.vm.provision "shell", run: "always", inline:<<-SCRIPT
            # Start dashboard service
            sudo systemctl start dashboard
        SCRIPT
    end
end
