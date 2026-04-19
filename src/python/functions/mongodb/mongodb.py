def install_mongodb():
    import subprocess
    import os
    # check if mongodb is installed
    res = os.system("mongod --version")
    if res == 0:
        print("MongoDB is already installed.")
    
    else:
        print("MongoDB is not installed. Installing MongoDB...")
        # install mongodb
        # source of installation guide: 
        # https://www.mongodb.com/docs/v7.0/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu
        
        # install packages if not present
        subprocess.run(["sudo", "apt-get", "install", "gnupg", "curl"])

        # import the MongoDB public GPG key
        subprocess.run([
            "curl", 
            "-fsSL", 
            "https://www.mongodb.org/static/pgp/server-7.0.asc", "|"
            "sudo", "gpg" ,"-o" ,
            "/usr/share/keyrings/mongodb-server-7.0.gpg",
            "--dearmor"
        ])

        # Create the list file for Ubuntu 22.04 (Jammy):
        subprocess.run([
            "echo", 
            "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse", "|",
            "sudo", "tee", "/etc/apt/sources.list.d/mongodb-org-7.0.list"
        ])

        # Reload the package database.
        subprocess.run(["sudo", "apt-get", "update"])

        # Install MongoDB community server
        subprocess.run(["sudo", "apt-get", "install", "-y", "mongodb-org"])

    
    # run mongodb
    subprocess.run(["sudo", "systemctl", "start", "mongod"])
    
    mdb_version = subprocess.check_output(["mongod", "--version"]).decode("utf-8")
    print(f"MongoDB version: {mdb_version}")
    

