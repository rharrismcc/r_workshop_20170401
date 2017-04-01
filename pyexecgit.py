import sys
import os

project = sys.argv[1]
os.system("cls")

def exec_git_clone(up, dirname, username, project):
	if up == 0:
		sdirname = "./{}".format(dirname)
	else:
		sdirname = "../{}".format(dirname)
		
	rmdirpath = "rmdir {} /S /Q".format(project)
	projectdir = "./{}".format(project)
	projectpath = "./{}/{}".format(dirname, project)
	gitpath = "git clone https://gitlab.com/{}/{}.git".format(username, project)
	os.chdir(sdirname)

	if os.path.isdir(projectdir):
		print('REMOVING PROJECT DIR  ' + rmdirpath)
		os.system(rmdirpath)

	os.system(gitpath)
	print(os.getcwd())

	
exec_git_clone(0, 'UserSubdirectoryName1','gitlabUsername1', project)
exec_git_clone(1, 'UserSubdirectoryName2','gitlabUsername2', project)
exec_git_clone(1, 'UserSubdirectoryName3','gitlabUsername3', project)
exec_git_clone(1, 'UserSubdirectoryName4','gitlabUsername4', project)
exec_git_clone(1, 'UserSubdirectoryName5','gitlabUsername5', project)
exec_git_clone(1, 'UserSubdirectoryName6','gitlabUsername6', project)
exec_git_clone(1, 'UserSubdirectoryName7','gitlabUsername7', project)
exec_git_clone(1, 'UserSubdirectoryName8','gitlabUsername8', project)
exec_git_clone(1, 'UserSubdirectoryName9','gitlabUsername9', project)
