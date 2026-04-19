def install_libraries(libs : list):
    import subprocess
    actual_libs = subprocess.run(["pip","list"], capture_output=True, text=True).stdout
    actual_libs = [lib.split(" ")[0] for lib in actual_libs.split("\n")[2:]]

    for lib in libs:
        if lib not in actual_libs:
            print("Installing library: ", lib)
            subprocess.run(["pip","install","-q",lib])

def check_requirements(file):
    with open(file, "r") as f:
        libs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return libs

    