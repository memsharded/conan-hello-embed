import os


def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


if __name__ == "__main__":
    system('git rev-parse HEAD > sha.txt')
    with open("sha.txt", "r") as f:
        sha = f.read().strip()
    os.unlink("sha.txt")
    system('conan export memsharded/%s' % sha)
    system('set CONAN_CHANNEL=%s && conan test' % sha)
