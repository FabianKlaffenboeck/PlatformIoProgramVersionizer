FILENAME_BUILDNO = 'versioning'
FILENAME_VERSION_H = 'include/version.h'
version = 'v0.1.'

import datetime
import subprocess


# this function gets the last Git commit hash and returns it
def get_git_revision_hash() -> str:
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    except:
        # when the project his is run on is not a Git Project the return an error massage
        return "This is no Project with Git enabled"


# try and get the version from the versioning file if there is no such file then crete it and start versioning from 1
build_no = 0
try:
    with open(FILENAME_BUILDNO) as f:
        build_no = int(f.readline()) + 1
except:
    print('Starting build number from 1..')
    build_no = 1
with open(FILENAME_BUILDNO, 'w+') as f:
    f.write(str(build_no))
    print('Build number: {}'.format(build_no))


# put together a the output that is writen to version.h file
hf = """
#ifndef BUILD_NUMBER
  #define BUILD_NUMBER "{}"
#endif
#ifndef GitHash
  #define GitHash "{}"
#endif
#ifndef VERSION
  #define VERSION "{} - {}"
#endif
#ifndef VERSION_SHORT
  #define VERSION_SHORT "{}"
#endif
""".format(build_no, get_git_revision_hash(), version + str(build_no), datetime.datetime.now(), version + str(build_no))
with open(FILENAME_VERSION_H, 'w+') as f:
    f.write(hf)
