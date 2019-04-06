from invoke import task
import re

@task
def buildlocal(ctx):
    ctx.run("docker build -t local/circleci-remote-docker:latest .")

@task
def testlocal(ctx):
    ctx.run("bash testlocal.sh")

@task
def evalpackages(ctx):
    ctx.run("docker build -t local/circleci-remote-docker:pinned . > result_log.pinned")
    ctx.run("docker build -f Dockerfile.unpinned -t local/circleci-remote-docker:latest . > result_log.latest")
    ctx.run('docker rmi local/circleci-remote-docker:pinned >> result_log.pinned')
    ctx.run('docker rmi local/circleci-remote-docker:latest >> result_log.latest')
    with open('result_log.latest', 'rU') as f_latest:
        print('%-25s %-20s %-20s') %('PACKAGE', 'LATEST', "PINNED")
        for line_latest in f_latest:
            if 'Installing' in line_latest:
                pkg_installed = re.search("Installing (.*)", line_latest).group(1)
                pkg_name_lastest = pkg_installed.split()[0]
                pvg_version_latest = re.search(re.escape('(')+"(.*)"+re.escape(')'),pkg_installed).group(1)
                pvg_version_pinned = 'not found'
                with open('result_log.pinned', 'rU') as f_pinned:
                    for line_pinned in f_pinned:
                        if 'Installing' in line_pinned:
                            pkg_installed = re.search("Installing (.*)", line_pinned).group(1)
                            pkg_name_pinned = pkg_installed.split()[0]
                            if pkg_name_pinned == pkg_name_lastest:
                                pvg_version_pinned = re.search(re.escape('(')+"(.*)"+re.escape(')'),pkg_installed).group(1)
                                break
                if pvg_version_latest != pvg_version_pinned:
                    print('%-25s %-20s \x1b[1;31;40m%-20s\x1b[0m') %(pkg_name_lastest, pvg_version_latest, pvg_version_pinned)
