#!/usr/bin/python

def attr():
	return {
		'general'	:	{
			'wait'	:	{
				'module'	:	'general.wait',
				'reference'	:	{
					'en'	:	'''
### Description
	wait for remote state(s) to complete, if anyone is not done yet, it will cause the host to block on the waiting.
	
### Parameters

*   **state** (*required*): one or multiple remote states to be waited
		example:
			single - @hostname.state_id
			barrier - @host1.state_1, @host2.state_2
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'state'	:	{
						'type'		:	'state',	# state is an array
						'required'	:	True,
						'visible'	:	True
					}
				}
			},
#			'reboot'	:	{
#				'module'	:	'general.reboot',
#				'reference'	:	{
#					'en'	:	'''
#### Description
#    perform a host reboot, note: do NOT reboot the host directly with cmd or script, which will be taken as the host crash
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					}
#				}
#			}
		},
		'common'	:	{
			'timezone'	:	{
				'module'	:	'common.timezone',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage the timezone
	
### Parameters

*   **name** (*required*): the timezone name
		   Pacific/Tahiti

*   **use utc** (*optional*): whether to use UTC for the hardware clock, by default ***True***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
						
					},
					'use utc'		:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					}
				}
			},
			'gem'	:	{
				'module'	:	'common.gem.package',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage ruby gems

### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'	:	{
						'type'		:	'dict',
						'option'	:	['latest', 'removed'],	# autofill options to show in IDE
						'default'	:	'',			# the default value to show in IDE,
						'required'	:	True,
						'visible'	:	True
					}
				}
			},
			'npm'	:	{
				'module'	:	'common.npm.package',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage node.js package (requires npm 1.2 or greater)

### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent

	note: the specified packages will be installed as global packages (npm install --global)

* **path** (*optional*): the path where the packages should be installed to
		note:
			if ignored, the packages will be installed as global packages (e.g. npm install --global)
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'	:	{
						'type'		:	'dict',
						'value'		:	['latest', 'removed'],	# values to show in IDE
						'default'	:	'',						# the default value of the item,
						'required'	:	True,
						'visible'	:	True
					},
					'path'	:	{
						'type'		:	'line',
						'required'	:	False,
						'visible'	:	True
					}
				}
			},
			#'pear'	:	{
			#	'module'	:	'package.pear.package',
			#	'reference'	:	{
			#		'en'	:	'''''',
			#		'cn'	:	''''''
			#	},
			#	'parameter'	:	{
			#		'name'	:	{
			#			'type'		:	'dict',
			#			'value'		:	['latest', 'removed'],	# values to show in IDE
			#			'default'	:	'',			# the default value of the item
			#			'required'	:	True
			#		}
			#	}
			#},
			#'pecl.package'	:	{
			#	'module'	:	'package.pecl.package',
			#	'reference'	:	{
			#		'en'	:	'''''',
			#		'cn'	:	''''''
			#	},
			#	'parameter'	:	{
			#		'name'	:	{
			#			'type'	:	'dict',
			#			'value'		:	['latest', 'removed'],	# values to show in IDE
			#			'default'	:	'',			# the default value of the item
			#			'required'	:	True
			#		}
			#	}
			#},
			'pip'	:	{
				'module'	:	'common.pip.package',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage pip packages

### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'	:	{
						'type'	:	'dict',
						'value'		:	['latest', 'removed'],	# values to show in IDE
						'default'	:	'',			# the default value of the item
						'required'	:	True,
						'visible'	:	True
					}
				}
			},
			'git'	:	{
				'module'	:	'common.git',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a git repo
	
### Parameters

* **path** (*required* ): the path to clone the repo
		example:
			/var/www/mysite/

*   **repo** (*required*): the git repository uri
		example:
			local - /opt/git/project.git or file:///opt/git/project.git
			ssh - ssh://user@server/project.git
			http/https - https://example.com/gitproject.git
			git - git://example.com/gitproject.git

* **branch** (*optional*): the branch to checkout
		example:
			master
	
		note:
			When using <branch>, the local repo will be kept synchronized with the latest commit of the specified branch.
			Do NOT use <branch> and <version> at the same time

* **version** (*optional*): the version to checkout
		example:
			tag name - release-1.0
			commit id - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6
	
		note:
			When using <version>, the local repo will remain the specified tag or commit.
			Do NOT use <branch> and <version> at the same time

* **ssh_key** (*optional*): the path of the ssh keypair file
		example:
			/root/.ssh/id_rsa

* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If so, the file owner will be left unchanged. If not, the file will be created under the user name of which the Madeira agent runs.

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If so, the file group will be left unchanged. If not, the file will be created under the group of which the Madeira agent runs.

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If so, the file mode will be left unchanged. If not, the file will be created with the default mode 0755

* **force** (*optional*): force the checkout even if there is conflict, by default ***False***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'repo'		:	{
						'type'		:	'line',
						'required'	:	True
					},
					'branch'	:	{
						'type'		:	'line',
						'default'	:	'master',
						'required'	:	False
					},
					'version'	:	{
						'type'		:	'line',
						'default'	:	'',
						'required'	:	False
					},
					'ssh key'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'force':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'hg'	:	{
				'module'	:	'common.hg',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a hg repo
	
### Parameters

* **path** (*required* ): the path to clone the repo
		example:
			/var/www/mysite/

*   **repo** (*required*): the hg repository uri
		example:
			local - /path/to/repo
			ssh - ssh://user@server/path/to/repo
			http/https - https://example.com/path/to/repo

* **branch** (*optional*): the branch to checkout
		example:
			default
	
		note:
			When using <branch>, the local repo will be kept synchronized with the latest commit of the specified branch.
			Do NOT use <branch> and <version> at the same time

* **revision** (*optional*): the version to checkout
		example:
			tag name - release-1.0
			changeset - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6
	
		note:
			When using <version>, the local repo will remain the specified tag or commit.
			Do NOT use <branch> and <version> at the same time

* **ssh_key** (*optional*): the path of the ssh keypair file
		example:
			/root/.ssh/id_rsa

* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If so, the file owner will be left unchanged. If not, the file will be created under the user name of which the Madeira agent runs.

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If so, the file group will be left unchanged. If not, the file will be created under the group of which the Madeira agent runs.

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If so, the file mode will be left unchanged. If not, the file will be created with the default mode 0755

* **force** (*optional*): force the checkout even if there is conflict, by default ***False***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'repo'		:	{
						'type'		:	'line',
						'required'	:	True
					},
					'branch'	:	{
						'type'		:	'line',
						'default'	:	'default',
						'required'	:	False
					},
					'revision'	:	{
						'type'		:	'line',
						'default'	:	'',
						'required'	:	False
					},
					'ssh key'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'force':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'svn'	:	{
				'module'	:	'common.svn',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a svn repo
	
### Parameters

* **path** (*required* ): the path to checkout the repo
		example:
			/var/www/mysite/

*   **repo** (*required*): the hg repository uri
		example:
			local - file:///path/to/repo
			http - http://example.com/path/to/repo
			https - https://example.com/path/to/repo
			svn - svn://example.com/path/to/repo
			svn+ssh - svn+ssh://user@example.com/path/to/repo

* **branch** (*optional*): the branch to checkout
		example:
			master
	
		note:
			When using <branch>, the local repo will be kept synchronized with the latest commit of the specified branch.
			Do NOT use <branch> and <version> at the same time

* **revision** (*optional*): the version to checkout
		example:
			tag name - release-1.0
			changeset - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6
	
		note:
			When using <version>, the local repo will remain the specified tag or commit.
			Do NOT use <branch> and <version> at the same time

* **username** (*optional*): the username of the svn server

* **password** (*optional*): the password of the svn user

* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If so, the file owner will be left unchanged. If not, the file will be created under the user name of which the Madeira agent runs.

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If so, the file group will be left unchanged. If not, the file will be created under the group of which the Madeira agent runs.

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If so, the file mode will be left unchanged. If not, the file will be created with the default mode 0755

* **force** (*optional*): force the checkout even if there is conflict, by default ***False***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'repo'		:	{
						'type'		:	'line',
						'required'	:	True
					},
					'branch'	:	{
						'type'		:	'line',
						'default'	:	'master',
						'required'	:	False
					},
					'revision'	:	{
						'type'		:	'line',
						'default'	:	'',
						'required'	:	False
						
					},
					'username'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'password'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'force':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'virtualenv'	:	{
				'module'	:	'common.virtualenv',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a python virtualenv
	
### Parameters

*   **path** (*required*): the environment path

*   **python** (*optional*): the python interpreter to use
		
		Note:
			python2.5 will use the python2.5 interpreter to create the new environment.
			The default is the interpreter that virtualenv was installed with

*   **requirements** (*optional*): the python requirements file path, which will be used to configure this environment

*   **system site packages** (*optional*): whether to give the virtual environment access to the global site-packages, by default ***True***

*   **always copy** (*optional*): whether to always copy files rather than symlinking, by default ***False***

*   **unzip setuptools** (*optional*): whether to always copy files rather than symlinking, by default ***False***

*   **no setuptool** (*optional*): whether to install setuptools (or pip) in the new virtualenv, by default ***True***

*   **no pip** (*optional*): whether to install pip in the new virtualenv, by default ***True***

*   **extra search dir** (*optional*): whether to always copy files rather than symlinking., by default ***False***

*   **always copy** (*optional*): the directories to look for setuptools/pip distributions in
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'python'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'requirements'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'system site packages'		:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					},
					'always copy'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'unzip setuptools'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'no setuptools'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'no pip'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'extra search dir'	:	{
						'type'		:	'array',
						'required'	:	False
					}
				}
			}
		},
		'linux'		:	{
			'apt pkg'	:	{
				'module'	:	'linux.apt.package',
				'distro'	:	['debian', 'ubuntu'],
				'reference'	:	{
					'en'	:	'''
### Description
	manage apt packages

### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent
	- **purged**: ensure the package is absent, and also delete all related configuration data of the package


* **repo** (*optional*): the repo name, which you want to use for installing the packages
		main

* **deb conf file** (*optional*): the Deb configuration file path
		/etc/apt/deb.conf
	
* **verify gpg** (*optional*): verify the package's GPG siganature, by default ***True***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'	:	{
						'type'	:	'dict',
						'option'	:	['latest', 'removed', 'purged'],	# autofill options to show in IDE
						'default'	:	'',			# the default value to show in IDE,
						'required'	:	True,
						'visible'	:	True
					},
					'repo'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'deb conf file'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'verify gpg':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'apt repo'	:	{
				'module'	:	'linux.apt.repo',
				'distro'	:	['debian', 'ubuntu'],
				'reference'	:	{
					'en'	:	'''
### Description
	manage apt repo

### Parameters

*   **name** (*required*): the repository name (/etc/apt/sources.list.d/$name.list will be crated)
		google

* **content** (*required*): the source list file content
		deb http://dl.google.com/linux/deb/ stable non-free
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'	:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'content'	:	{
						'type'	:	'line',
						'required'	:	True
					}
				}
			},
			'yum package'	:	{
				'module'	:	'linux.yum.package',
				'distro'	:	['amazon', 'redhat', 'centos'],
				'reference'	:	{
					'en'	:	'''
### Description
	manage yum packages

### Parameters

*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
	- **removed**: ensure the package is absent
	- **purged**: ensure the package is absent, and also delete all related configuration data of the package

* **repo** (*optional*): the repo name, which you want to use for installing the packages
		epel
	
* **verify gpg** (*optional*): verify the package's GPG siganature, by default ***True***
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'	:	{
						'type'	:	'dict',
						'value'		:	['latest', 'removed'],	# values to show in IDE
						'default'	:	'',			# the default value of the item
						'required'	:	True,
						'visible'	:	True
					},
					'repo'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'verify gpg'	:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					}
				}
			},
			'yum repo'	:	{
				'module'	:	'linux.yum.repo',
				'distro'	:	['amazon', 'redhat', 'centos'],
				'reference'	:	{
					'en'	:	'''
### Description
	manage a yum repo

### Parameters

*   **name** (*required*): the repo name
		   epel
 
* **content** (*required*): the content of the repo configuration file 
		[10gen]
		name=10gen Repository
		baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/i686
		gpgcheck=0
		enabled=1
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'content'	:	{
						'type'		:	'line',
						'required'	:	True
					}
				}
			},
#			'zypper package'	:	{
#				'module'	:	'linux.zypper.package',
#				'distro'	:	['opensuse', 'suse'],
#				'reference'	:	{
#					'en'	:	'''
#### Description
#	manage zypper packages
#
#### Parameters
#
#*   **name** (*required*): the package names and versions. You can specify multiple pakages. The following values can be used for package version:
#	- <***empty***> (*default*): ensure the package is installed. If not, will install the latest version available of all APT repos on                   
#	- <***version***>: ensure the package is installed, with the version specified. If the version in unavailable of all APT repos on the host, the state will fail
#	- **latest**: ensure the package is installed with the latest version. If a newer version is available of all APT repos on the host, will do a auto-upgrade
#	- **removed**: ensure the package is absent
#	- **purged**: ensure the package is absent, and also delete all related configuration data of the package
# 
#
#* **fromrepo** (*optional*): an repo name, which you want to use for installing the packages
#		epel
#	
#* **verify gpg** (*optional*): verify the package's GPG siganature, by default ***True***
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					'name'	:	{
#						'type'	:	'dict',
#						'value'		:	['latest', 'removed'],	# values to show in IDE
#						'default'	:	'',			# the default value of the item
#						'required'	:	True
#					},
#					'fromrepo'		:	{
#						'type'		:	'line',
#						'required'	:	False
#					},
#					'verify gpg'	:	{
#						'type'		:	'bool',
#						'default'	:	True,
#						'required'	:	False
#					}
#				}
#			},
#			'zypper repo'	:	{
#				'module'	:	'linux.zypper.repo',
#				'distro'	:	['opensuse', 'suse'],
#				'reference'	:	{
#					'en'	:	'''
#### Description
#	manage zypper repo
#
#### Parameters
#
#*   **name** (*required*): the repo name
#		   packman
# 
#
#* **url** (*required*): the repo url
#		http://ftp.gwdg.de/pub/linux/packman/suse/13.1/
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					'name'		:	{
#						'type'		:	'line',
#						'required'	:	True
#					},
#					'url'	:	{
#						'type'		:	'line',
#						'required'	:	True
#					}
#				}
#			},
			'dir'	:	{
				'module'	:	'linux.dir',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a directory

### Parameters

*   **path** (*required*): the directory path
		example:
			/var/www/html

		note:
			This state ensures the specifed directory is present with correposnding attributes. If the parent directory is present, its attributes will be left unchanged, otherwise it will be created with the same attributed of the specified directory itself.
 
* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **recursive** (*optional*): whehther to recursively set attributes of all sub-directories under *path*, by default ***True***

* **absent** (*optional*): ensure the directory is absent, by default ***False***
		note:
			If True, all other parameters are ignored
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'recursive'	:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					},
					'absent'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'file'	:	{
				'module'	:	'linux.file',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a file

### Parameters

*   **path** (*required*): the file path
		example:
			/root/.ssh/known_hosts

		note:
			This state ensures the specifed file is present with correposnding attributes and content. If the directory is present, its attributes will be left unchanged, otherwise it will be created with the same attributed of the specified file itself.
 
* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **content** (*optional*): the file content
		note:
			If the specified file exists, the file will be reset, otherwise the file will be created with this content

* **absent** (*optional*): ensure the directory is absent, by default ***False***
		note:
			If True, all other parameters are ignored
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'	:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'content'	:	{
						'type'		:	'text',
						'required'	:	False
					},
					'absent'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
						'visible'	:	True,
					}
				}
			},
			'symlink'	:	{
				'module'	:	'linux.symlink',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a symlink

### Parameters

*   **source** (*required*): the path to link to
		example:
			/data/
 
* **target** (*required*): the path to the symlink
		example:
			/mnt/data/
	
		note:
			If the target's parent path does not exist, this state will fail.

* **user** (*optional*): the user name of the file owner
		example:
			root
	
		note:
			If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists. If existed, the file owner will be left unchanged, otherwise default: root

* **group** (*optional*): the group name of the file owner
		example:
			root
	
		note:
			If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists. If existed, the file group will be left unchanged; otherwise default: root

* **mode** (*optional*): the directory mode
		example:
			0755
	
		note:
			If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists. If existed, the file mode will be left unchanged, otherwise default: 0755

* **absent** (*optional*): ensure the directory is absent, by default ***False***
		note:
			If True, all other parameters are ignored
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'source'		:	{
						'type'		:	'line',
						'required'	:	False,
						'visible'	:	True,
					},
					'target'	:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'group'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'mode':	{
						'type'		:	'line',
						'default'	:	'0755',
						'required'	:	False
					},
					'absent'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
						'visible'	:	True
					}
				}
			},
			'service'	:	{
				'module'	:	'linux.service',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage system service
	
### Parameters

*   **name** (*required*): the service name
		example:
			httpd

*   **watch** (*optional*): watch a list of files or directories, restart the service if any of them is modified
		example:
			/etc/nginx/nginx.conf, /etc/my.cnf
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'		:	'array',
						'required'	:	True,
						'visible'	:	True
					},
					'watch'		:	{
						'type'		:	'array',
						'required'	:	False,
						'visible'	:	True
					}
				}
			},
			'supervisord'	:	{
				'module'	:	'linux.supervisord',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage supervisord service
	
### Parameters

*   **name** (*required*): the service name
		example:
			httpd

*   **config** (*required*): the path of supervisord configuration file
		example:
			/etc/supervisord

		note:
			When this file is modified, supervisord will be restarted, which causes all managed services restarted

*   **watch** (*optional*): watch a list of files or directories, restart the service if any of them is modified
		example:
			/etc/nginx/nginx.conf, /etc/my.cnf
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'		:	'array',
						'required'	:	True,
						'visible'	:	True,
					},
					'watch'		:	{
						'type'		:	'array',
						'required'	:	False,
						'visible'	:	True
					},
					'config'	:	{
						'type'		:	'line',
						'required'	:	True
					}
				}
			},
			'cron'	:	{
				'module'	:	'linux.cron',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage cron jobs
	
### Parameters

*   **user** (*optional*): the user to execute the cron job, by default: root

*   **cmd** (*required*): the command to execute
		example:
			cat /proc/meminfo >> /tmp/meminfo

*   **minute** (*optional*): 0 - 59

*   **hour** (*optional*): 0 - 23 (must be a valid day if a month is specified)

*   **day of month** (*optional*): 1 - 31

*   **month** (*optional*): 1 - 12

*   **day of week** (*optional*): 0 - 7, sunday is represented by 0 or 7, monday by 1
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'minute'	:	{
						'type'		:	'line',
						'option'	:	['*'],
						'required'	:	False
					},
					'hour'	:	{
						'type'		:	'line',
						'option'	:	['*'],
						'required'	:	False
					},
					'day of month'	:	{
						'type'		:	'line',
						'option'	:	['*'],
						'required'	:	False
					},
					'month'	:	{
						'type'		:	'line',
						'option'	:	['*'],
						'required'	:	False
					},
					'day of week'	:	{
						'type'		:	'line',
						'option'	:	['*'],
						'required'	:	False
					},
					'user'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'cmd'	:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					}
				}
			},
#			'fs'	:	{
#				'module'	:	'linux.fs',
#				'distro'	:	None,
#				'reference'	:	{
#					'en'	:	'''
#### Description
#	manage the filesystem
#	
#### Parameters
#
#*   **dev** (*required*): the device name
#		example:
#			/dev/sda1
#
#*   **filesystem** (*required*): the filesystem type of the device    
#
#*   **force** (*optional*): forcefully create the new filesystem, even if there is already one on the specified device, by default *False*
#
#*   **opts** (*optional*): additional options for creating the filesystem, see *MKE2FS(8)*
#			example:
#				-O journal_dev [ -b block-size ] [ -L volume-label ] [ -n ] [ -q ] [ -v ]  external-journal [ blocks-count ]
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					'dev'	:	{
#						'type'		:	'line',
#						'required'	:	True,
#						'visible'	:	True
#					},
#					'filesystem':	{
#						'type'		:	'line',
#						'option'	:	['ext2', 'ext3', 'ext4', 'btrfs', 'reiserfs', 'xfs', 'zfs'],
#						'required'	:	True,
#						'visible'	:	True
#					},
#					'opts':	{
#						'type'		:	'line',
#						'required'	:	False
#					},
#					'force'		:	{
#						'type'		:	'bool',
#						'default'	:	True,
#						'required'	:	False
#					}
#				}
#			},
#			'hosts'	:	{
#				'module'	:	'linux.hosts',
#				'distro'	:	None,
#				'reference'	:	{
#					'en'	:	'''
#### Description
#	manage /etc/hosts
#	
#### Parameters
#
#*   **ip** (*required*): the IP address
#
#*   **hostnames** (*required*): a list of hostnames
#		example:
#			web, web.example.com
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					'ip'	:	{
#						'type'		:	'line',
#						'required'	:	True
#					},
#					'hostnames'	:	{
#						'type'		:	'array',
#						'required'	:	True
#					},
#				}
#			},
#			'hostname'	:	{
#				'module'	:	'linux.hostname',
#				'distro'	:	None,
#				'reference'	:	{
#					'en'	:	'''
#### Description
#	manage hostname
#
#### Parameters
#
#*   **hostname** (*required*): the hostname
#					''',
#					'cn'	:	''''''
#				},
#				'parameter'	:	{
#					'hostname'	:	{
#						'type'		:	'line',
#						'required'	:	True,
#						'visible'	:	True
#					}
#				}
#			},
			'mount'	:	{
				'module'	:	'linux.mount',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage mount points (/etc/fstab)
	
### Parameters

*   **path** (*required*): the path of the mount point

*   **device** (*required*): the device name

*   **filesystem** (*required*): the file system type of the device

*   **dump** (*optional*): the dump value in /etc/fstab, see *fstab(8)*

*   **passno** (*optional*): the pass value in /etc/fstab, see *fstab(8)*

*   **opts** (*optional*): a list of options for /etc/fstab
			example:
				noatime
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'device'	:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'filesystem':	{
						'type'		:	'line',
						'option'	:	['ext2', 'ext3', 'ext4', 'btrfs', 'iso9660', 'ntfs', 'reiserfs', 'xfs', 'zfs'],
						'required'	:	True
					},
					'dump':	{
						'type'		:	'line',
						'default'	:	'0',
						'required'	:	False
					},
					'passno':	{
						'type'		:	'line',
						'default'	:	'0',
						'required'	:	False
					},
					'opts':	{
						'type'		:	'line',
						'required'	:	False
					}
				}
			},
			'cmd'	:	{
				'module'	:	'linux.cmd',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	execute a shell command
	
### Parameters

*   **cmd** (*required*): the command to execute
		example:
			find . -name *.pyc | xargs rm

*   **cwd** (*optional*): the current working directory to execute the command, be default */madeira/tmp/*

*   **user** (*optional*): the user to execute the command, be default the user which the agent runs as

*   **group** (*optional*): the group to execute the command, be default the group which the agent runs as

*   **env** (*optional*): environment variables for the command

*   **timeout** (*optional*): command timeout, by default *600* (in seconds)
		note:
			By default, a command will be terminated and taken "failed" if not finishe in 600 seconds. However you can change with    this option.

*   **with_path** (*optional*): the command will not run if the specified path exists

*   **without_path** (*optional*): the command will not run if the specified path does not exist
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'bin'		:	{
						'type'		:	'line',
						'option'	:	'',
						'default'	:	'bin/sh',
						'required'	:	False
					},
					'cmd'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'cwd'		:	{
						'type'		:	'line',
						'default'	:	'/madeira/tmp/',
						'required'	:	False
					},
					'user'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'group'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'timeout'	:	{
						'type'		:	'line',
						'default'	:	600,
						'required'	:	True
					},
					'env'		:	{
						'type'		:	'dict',
						'required'	:	False
					},
					'with_path'	:	{
						'type'		:	'line',
						'required'	:	False,
						'visible'	:	True
					},
					'without_path'	:	{
						'type'		:	'line',
						'required'	:	False,
						'visible'	:	True
					}
				}
			},
			'user'	:	{
				'module'	:	'linux.user',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a user
	
### Parameters

*   **username** (*required*): the user name

*   **password** (*required*): the encrypted value of the password
		note:
			use "openssl passwd -salt <salt> -1 <plaintext>" to generate the passworld hash

*   **fullname** (*optional*): the full name of the user

*   **uid** (*optional*): the user id

*   **gid** (*optional*): the group id

*   **home** (*optional*): the home directory of the user, by default: ***/home/$username***
		note:
			if the directory already exists, the user and group of the directory will be set to this user; otherwise, the directory (and its parent directories) will be created, with the user and group of the user.

*   **nologin** (*optional*): whether to allow user to login, by default *False*

*   **groups** (*optional*): a list of groups of the user
		note:
			if pass in an empty list, all groups of the user will be removed except the defaut one
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'username'	:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'password'	:	{
						'type'		:	'line',
						'required'	:	True
					},
					'fullname'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'uid'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'gid'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'home'		:	{
						'type'		:	'line',
						'default'	:	'/home/$username',		# TODO:
						'required'	:	False,
						'visible'	:	True
					},
					'nologin'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'groups'	:	{
						'type'		:	'array',
						'required'	:	False
					},
				}
			},
			'group'	:	{
				'module'	:	'linux.group',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage a group
	
### Parameters

*   **groupname** (*required*): the group name

*   **gid** (*optional*): the group id

*   **system** (*optional*): whether this is a system group, by default *False*
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'groupname'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'gid'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'system'		:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'pv'	:	{
				'module'	:	'linux.lvm.pv',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage LVM physical volume (PV)
	
### Parameters

*   **path** (*required*): the path of the device or partition

		Example:
			/dev/sdc4, /dev/sde

*   **force** (*optional*): force to create the PV without any confirmation, by default ***False***

		Note:
			You can not recreate (reinitialize) a PV belonging to an existing volume group. 


*   **uuid** (*optional*): specify the uuid for the device

		Note:
			Without this option, a random uuid will be generated. All of your PVs must have unique uuids. You need to use
			this option before restoring a backup of LVM metadata onto a replacement device - see vgcfgrestore(8). As such, 
			use of ***restore file is compulsory unless the norestorefile is used.


*   **zero** (*optional*): whether or the first 4 sectors (2048 bytes) of the device should be wiped, by default ***True***

		Note:
			If this option is not given, the default is to wipe these sectors unless either or both of the --restorefile or
			--uuid options were specified.

*   **data alignment** (*optional*): align the start of the data to a multiple of this number

		Note:
			You should also specify an appropriate "PV size" when creating the Volume Group (VG).
			To  see the location of the first Physical Extent of an existing
			Physical Volume use pvs -o +pe_start .  It will be a multiple of
			the  requested  alignment.   In  addition  it  may be shifted by
			alignment_offset   from   data_alignment_offset_detection    (if
			enabled in lvm.conf(5)) or --dataalignmentoffset.

*   **data alignment offset** (*optional*): shift the start of the data area by this additional number

*   **metadata size** (*optional*): the approximate amount of space to be set aside for each metadata area

		Note:
			The size you specify may get rounded

*   **metadata type** (*optional*): specify which type of on-disk metadata to use, by default ***lvm2***

		Example:
			lvm1, lvm2, 1, 2

		Note:
			lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format
			in the global section of the config file.

*   **metadata copies** (*optional*): the number of metadata areas to set aside on each PV

		Example:
			Currently this  can  be  0, 1 or 2

		Note:
			If set to 2, two copies of the volume group metadata are held on the PV, one at the front  of  the  PV
			and one at the end.  If set to 1 (the default), one copy is kept
			at the front of the PV (starting in the 5th sector).  If set  to
			0,  no  copies  are kept on this PV - you might wish to use this
			with VGs containing large numbers of PVs.  But if  you  do  this
			and  then  later  use vgsplit(8) you must ensure that each VG is
			still going to have a suitable number of copies of the  metadata
			after the split!


*   **metadata ignore** (*optional*): whether to ignore metadata areas on this PV, by default ***False***

		Note:
			This setting can be changed with pvchange.   If
			metadata  areas  on  a physical volume are ignored, LVM will not
			store metadata in the metadata areas present  on  this  Physical
			Volume.   Metadata  areas  cannot  be  created or extended after
			Logical Volumes have been allocated on the device. If you do not
			want  to  store metadata on this device, it is still wise always
			to allocate a metadata area in case you need it  in  the  future
			and to use this option to instruct LVM2 to ignore it.


*   **restore file** (*optional*):

		Note:
			In conjunction with "uuid", this extracts the location and size
			of the data on the PV from the file  (produced  by  vgcfgbackup)
			and  ensures  that  the  metadata  that  the program produces is
			consistent with the contents  of  the  file  i.e.  the  physical
			extents will be in the same place and not get overwritten by new
			metadata.  This provides a mechanism  to  upgrade  the  metadata
			format  or to add/remove metadata areas. Use with care. See also
			vgconvert(8).

*   **no restore file** (*optional*):

		Note:
			In conjunction with "uuid", this allows a uuid to  be  specified
			without  also  requiring  that  a  backup  of  the  metadata  be
			provided.

*   **label sector** (*optional*):

		Note:
			By default the PV is labelled with an  LVM2  identifier  in  its
			second  sector (sector 1).  This lets you use a different sector
			near the start of the disk (between 0  and  3  inclusive  -  see
			LABEL_SCAN_SECTORS in the source).  Use with care.

*   **PV size** (*optional*):

		Note:
			Overrides  the  automatically-detected size of the PV, use with care
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'array',
						'required'	:	True,
						'visible'	:	True
					},
					'force'		:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					},
					'uuid'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'zero'		:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					},
					'data alignment'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'metadata size'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'data alignment offset'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'metadata type'	:	{
						'type'		:	'line',
						'default'	:	'lvm2',
						'option'	:	['lvm1', 'lvm2'],
						'required'	:	False
					},
					'metadata copies'	:	{
						'type'		:	'line',
						'option'	:	['0', '1', '2'],
						'required'	:	False
					},
					'metadata ignore'	:	{
						'type'		:	'bool',
						'dfault'	:	False,
						'required'	:	False
					},
					'restorefile'	:	{
						'type'		:	'line',
						'required'	:	False
					},
					'norestorefile'	:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					},
					'label sector'	:	{
						'type'		:	'line',
						'default'	:	'LVM2',
						'required'	:	False
					},
					'PV size'		:	{
						'type'		:	'line',
						'required'	:	False
					}
				}
			},
			'vg'	:	{
				'module'	:	'linux.lvm.vg',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage LVM volume group (VG)
	
### Parameters


*   **name** (*required*): the VG name

*   **path** (*required*): a list of block special devices

		Example:
			/dev/sdk1, /dev/sdl1

*   **clustered** (*optional*): whether to enable the clustered locking on the VG, by default ***True***

		Note:
			If the new VG is shared with other nodes in the cluster, need to enable this option
			If the new VG contains only local disks that are not visible on the other nodes, this option must be turned off
			If the cluster infrastructure is unavailable on a particular node at a particular time, you may still be able to 
			use such VGs

*   **max LV number** (*optional*): specify the maximum number of LVs allowed in this VG

		Note:
			For VGs with  metadata in lvm1 format, the limit and default value is 255
			If the metadata uses lvm2 format, the default value is 0 which removes this restriction: there is then no limit

*   **max PV number** (*optional*): specify the maximum number of PVs that can belong to this VG

		Note:
			For VGs with metadata in lvm1 format, the limit and default value is 255
			If the metadata uses lvm2 format, the value 0 removes this restriction: there is then no limit


*   **max PV number** (*optional*): specify the maximum number of PVs that can belong to this VG

		Note:
			For VGs with metadata in lvm1 format, the limit and default value is 255
			If the metadata uses lvm2 format, the value 0 removes this restriction: there is then no limit

*   **metadata type** (*optional*): specify which type of on-disk metadata to use, by default ***lvm2***

		Example:
			lvm1, lvm2, 1, 2

		Note:
			lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format
			in the global section of the config file.

*   **metadata copies** (*optional*): specify the desired number of metadata copies in the VG

		Example:
			unmanaged, all

		Note:
			If set to a non-zero value, LVM will automatically manage the 'metadata ignore' option on the PVs (see pvcreate(8) or pvchange --metadataignore) in order to achieve the copies of metadata. If set to unmanaged, LVM will not automatically manage the 'metadata ignore' option. If set to all, LVM will first clear all of the 'metadata ignore' option on all metadata areas in the VG, then set the value to unmanaged. This option is useful for VGs containing large numbers of PVs   with metadata  as  it may be used to minimize metadata read and write overhead.  The default value is unmanaged



*   **PE size** (*optional*): specify the physical extent size on PVs of this VG

		Example:
			bBsSkKmMgGtTpPeE

		Note:
			A size suffix (k for kilobytes up to t for terabytes) is optional, megabytes is the default if no suffix is present. The default is 4 MiB and it must be at least 1 KiB and a power of 2.

			  Once  this  value  has  been  set,  it is difficult to change it
			  without recreating the volume group which would involve  backing
			  up  and  restoring  data on any logical volumes.  However, if no
			  extents need moving for the  new  value  to  apply,  it  can  be
			  altered using vgchange -s.

			  If  the volume group metadata uses lvm1 format, extents can vary
			  in size from 8KiB to 16GiB and there is a limit of 65534 extents
			  in each logical volume.  The default of 4 MiB leads to a maximum
			  logical volume size of around 256GiB.

			  If the volume group metadata uses lvm2 format those restrictions
			  do  not  apply,  but  having a large number of extents will slow
			  down the tools but have no impact  on  I/O  performance  to  the
			  logical volume.  The smallest PE is 1KiB

			  The 2.4 kernel has a limitation of 2TiB per block device.

*   **autobackup** (*optional*): whether to  metadata should be backed up automatically after a change, by default ***True***

		Note:
			You are strongly advised not to  disable  this! See vgcfgbackup(8)

*   **tag** (*optional*): add the tag to this VG 

		Note:
			A tag is a
			  word that can be used to group LVM2 objects  of  the  same  type
			  together.  Tags can be given on the command line in place of PV,
			  VG or LV arguments.  Tags should be prefixed  with  @  to  avoid
			  ambiguity.   Each  tag  is  expanded  by  replacing  it with all
			  objects possessing that tag which are of the  type  expected  by
			  its  position  on  the  command line.  PVs can only possess tags
			  while they are part of a Volume Group: PV tags are discarded  if
			  the  PV  is  removed  from the VG.  As an example, you could tag
			  some LVs as database and others as userdata  and  then  activate
			  the  database  ones  with  lvchange  -ay @database.  Objects can
			  possess  multiple  tags  simultaneously.   Only  the  new   LVM2
			  metadata   format  supports  tagging:  objects  using  the  LVM1
			  metadata format cannot be tagged because the on-disk format does
			  not support it.  Characters allowed in tags are: A-Z a-z 0-9 _ +
			  . - and as of version 2.02.78 the following characters are  also
			  accepted: / = ! : # &

*   **allocation policy** (*optional*): specify the allocation policy

		Example:
			contiguous,  cling,  normal, anywhere or inherit

		Note:
			When a command needs to allocate  Physical
			  Extents  from  the  Volume Group, the allocation policy controls
			  how they are chosen.  Each Volume Group and Logical  Volume  has
			  an allocation policy defined.  The default for a Volume Group is
			  normal which applies common-sense  rules  such  as  not  placing
			  parallel stripes on the same Physical Volume.  The default for a
			  Logical Volume is inherit which applies the same policy  as  for
			  the   Volume   Group.   These  policies  can  be  changed  using
			  lvchange(8) and vgchange(8) or overridden on the command line of
			  any  command  that  performs  allocation.  The contiguous policy
			  requires  that  new  Physical  Extents  be  placed  adjacent  to
			  existing Physical Extents.  The cling policy places new Physical
			  Extents on the same Physical Volume as existing Physical Extents
			  in  the  same  stripe  of  the  Logical  Volume.   If  there are
			  sufficient  free  Physical  Extents  to  satisfy  an  allocation
			  request  but  normal  doesn't  use them, anywhere will - even if
			  that reduces performance by placing  two  stripes  on  the  same
			  Physical Volume.
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'name'		:	{
						'type'		:	'line',
						'required'	:	True,
						'visible'	:	True
					},
					'path'		:	{
						'type'		:	'array',
						'required'	:	True,
						'visible'	:	True
					},
					'clustered'		:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False
					},
					'max LV number'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'max PV number'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'metadata type'	:	{
						'type'		:	'line',
						'default'	:	'lvm2',
						'option'	:	['lvm1', 'lvm2'],
						'required'	:	False
					},
					'metadata copies'		:	{
						'type'		:	'line',
						'option'	:	['unmanaged', 'all'],
						'required'	:	False
					},
					'PE size'		:	{
						'type'		:	'line',
						'default'	:	'4m',
						'required'	:	False
					},
					'tag'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'allocation policy'		:	{
						'type'		:	'line',
						'option'	:	['anywhere', 'contiguous', 'cling', 'inherit', 'normal'],
						'required'	:	False
					},
					'autobackup'		:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
			'lv'	:	{
				'module'	:	'linux.lvm.lv',
				'distro'	:	None,
				'reference'	:	{
					'en'	:	'''
### Description
	manage LVM logical volume (LV)
	
### Parameters

*   **path** (*required*): a list of block special devices

		Example:
			/dev/sdk1, /dev/sdl1

		Note:
		VolumeGroup{Name|Path}[/ThinPoolLogicalVolumeName]
	   [PhysicalVolumePath[:PE[-PE]]...]

*   **name** (*optional*): specify the name of the new LV

		Note:
			Without this option a default names of "lvol#" will be generated where # is the LVM internal number of the logical volume

*   **available** (*optional*): specify the name of the new LV

		Example:
			y, ay, n, ey, en, ly, ln

		Note:
			Controls  the  availability of the Logical Volumes for immediate
			  use after the command finishes running.  By default, new Logical
			  Volumes are activated (-ay).  If it is possible technically, -an
			  will leave the new Logical Volume  inactive.  But  for  example,
			  snapshots  can only be created in the active state so -an cannot
			  be used with --snapshot.  Normally the --zero n argument has  to
			  be  supplied  too  because  zeroing (the default behaviour) also
			  requires activation.  If autoactivation option is  used  (-aay),
			  the  logical  volume  is activated only if it matches an item in
			  the activation/auto_activation_volume_list set in lvm.conf.  For
			  autoactivated logical volumes, --zero n is always assumed and it
			  can't be overridden. If clustered locking is enabled, -aey  will
			  activate  exclusively on one node and -aly will activate only on
			  the local node.

*   **chunk size** (*optional*): speicy the size of chunk for snapshot and thin pool LV

		Note:
			For  snapshots  the  value must be power of 2 between
			  4KiB and 512KiB and the default value is 4.  For thin pools  the
			  value must be between 64KiB and 1048576KiB and the default value
			  starts with 64 and scales up  to  fit  the  pool  metadata  size
			  within  128MB, if the poolmetadata size is not specified.  Older
			  dm thin pool target version (<1.4)  requires  the  value  to  be
			  power  of  2.   The newer version requires to be the multiple of
			  64KiB, however discard is not  supported  for  non  power  of  2
			  values.  Default unit is in kilobytes.


*   **contiguous** (*optional*): set or reset the contiguous allocation policy for LVs, by default ***False***

		Note:
			Default is no contiguous allocation  based  on  a  next
			  free principle.

*   **discards** (*optional*): specify the discards behavior, by default ***passdown***

		Example:
			ignore, nopassdown, passdown
			  

*   **stripe number** (*optional*): specify the number of stripes

		Note:
			This is equal to the number of physical volumes to scatter the logical volume

*   **stripe size** (*optional*): specify the  number  of  kilobytes  for  the  granularity  of  the stripes.

		Note:
			  size must be 2^n (n = 2 to 9) for metadata in LVM1 format.
			  For metadata in LVM2 format, the stripe size  may  be  a  larger
			  power of 2 but must not exceed the physical extent size


*   **LE number** (*optional*): specify the  number  of  logical  extents to allocate for the new LV

		Note:
			The  number  can  also  be  expressed  as   a
			  percentage  of  the  total  space  in  the Volume Group with the
			  suffix %VG, as a percentage of the remaining free space  in  the
			  Volume  Group  with  the  suffix  %FREE,  as a percentage of the
			  remaining free space for the  specified  PhysicalVolume(s)  with
			  the  suffix  %PVS,  or  (for  a snapshot) as a percentage of the
			  total space  in  the  Origin  Logical  Volume  with  the  suffix
			  %ORIGIN

*   **LV size** (*optional*): specify the  size to allocate for the new LV

		Note:
			A size suffix of K for kilobytes, M for megabytes, G for  gigabytes,  T
			  for terabytes, P for petabytes or E for exabytes is optional.
			  Default unit is megabytes

*   **minor number** (*optional*): specify the minor number

*   **persistent** (*optional*): whether to make the minor number specified persistent, by default ***False***

		Note:
			Set to y to 

*   **mirror number** (*optional*): Create a mirrored LV with this number of copies

		Note:
			  For example, specifying "-m 1" would result in a  mirror  with  two-
			  sides; that is, a linear volume plus one copy.

			  Specifying   the  optional  argument  --nosync  will  cause  the
			  creation of the mirror to skip  the  initial  resynchronization.
			  Any  data  written afterwards will be mirrored, but the original
			  contents will not be copied.  This  is  useful  for  skipping  a
			  potentially long and resource intensive initial sync of an empty
			  device.

			  The optional argument --mirrorlog specifies the type of  log  to
			  be  used.  The default is disk, which is persistent and requires
			  a small amount of storage space, usually on  a  separate  device
			  from  the  data  being mirrored.  Using core means the mirror is
			  regenerated by copying the data from the first device again each
			  time  the  device is activated, for example, after every reboot.
			  Using "mirrored" will create a persistent  log  that  is  itself
			  mirrored.

			  The  optional  argument  --corelog  is equivalent to --mirrorlog
			  core

*   **no udev sync** (*optional*): whether to disable udev synchronisation, by default ***False***

		Note:
			The  process  will not wait for
			  notification from udev.  It will continue  irrespective  of  any
			  possible udev processing in the background.  You should only use
			  this if udev is not running or has rules that ignore the devices
			  LVM2 creates

*   **monitor** (*optional*): whether to monitor a mirrored or snapshot LV with dmeventd, if it is installed, by default ***False***

		Note:
			If  a  device  used  by  a
			  monitored  mirror  reports  an I/O error, the failure is handled
			  according        to        mirror_image_fault_policy         and
			  mirror_log_fault_policy set in lvm.conf

*   **ignore monitoring** (*optional*): make no attempt to interact with dmeventd unless ***monitor*** is ***True*** ,by default ***False***

*   **permission** (*optional*): specify the access permissions to read only or read and write, by default ***RW***

		Example:
			r, rw

*   **pool metadata size** (*optional*): specify the size of thin pool's metadata LV

		Note:
			Supported value  is  in  range  between  2MiB and 16GiB.  Default value is
			  (Pool_LV_size / Pool_LV_chunk_size  *  64b).   Default  unit  is
			  megabytes.

*   **region size** (*optional*):

		Note:
			 A  mirror  is divided into regions of this size (in MB), and the
			  mirror log uses this granularity to track which regions  are  in
			  sync.

*   **readahead** (*optional*): set read ahead sector count of this LV

		Example:
			ReadAheadSectors, auto, none

		Note:
			  For volume groups with metadata in  lvm1  format,  this  must  be  a  value
			  between 2 and 120.  The default value is "auto" which allows the
			  kernel to choose a  suitable  value  automatically.   "None"  is
			  equivalent to specifying zero.

*   **snapshot** (*optional*): create  a snapshot logical volume (or snapshot) for an existing, so  called  original  logical  volume  (or  origin)

		Note:
			Snapshots
			  provide a 'frozen image' of the contents of the origin while the
			  origin can still be updated. They enable consistent backups  and
			  online   recovery   of   removed/overwritten  data/files.   Thin
			  snapshot is created when the origin is a  thin  volume  and  the
			  size  is  not specified. Thin snapshot shares same blocks within
			  the thin pool volume.  The snapshot with the specified size does
			  not need the same amount of storage the origin has. In a typical
			  scenario, 15-20% might be enough.  In case the snapshot runs out
			  of  storage, use lvextend(8) to grow it. Shrinking a snapshot is
			  supported by  lvreduce(8)  as  well.  Run  lvdisplay(8)  on  the
			  snapshot  in  order  to  check how much data is allocated to it.
			  Note that a small amount  of  the  space  you  allocate  to  the
			  snapshot  is  used to track the locations of the chunks of data,
			  so you should allocate slightly more  space  than  you  actually
			  need  and monitor the rate at which the snapshot data is growing
			  so you can avoid running out of space

*   **thinpool** (*optional*): Creates thin pool or thin logical volume  or  both

		Example:
			ReadAheadSectors, auto, none

		Note:
			.   Specifying
			  the optional argument --size will cause the creation of the thin
			  pool  logical  volume.    Specifying   the   optional   argument
			  --virtualsize will cause the creation of the thin logical volume
			  from given thin pool volume.   Specifying  both  arguments  will
			  cause  the creation of both thin pool and thin volume using this
			  pool.   Requires  device   mapper   kernel   driver   for   thin
			  provisioning from kernel 3.2 or newer

*   **type** (*optional*): Create  a  logical  volume  that uses the specified segment type, (e.g. "raid5", "mirror", "snapshot", "thin", "thin-pool")

		Note:
			Many segment  types  have a commandline switch alias that will enable
			  their use (-s is an alias for --type snapshot).   However,  this
			  argument  must be used when no existing commandline switch alias
			  is available for the desired type, as is the  case  with  error,
			  zero, raid1, raid4, raid5 or raid6

*   **virtual size** (*optional*): Create  a  sparse  device  of  the given size (in MB by default) using a snapshot or thinly provisioned device when thin pool  is specified.  

		Note:
			Anything written to the device will be returned when
			  reading from it.  Reading from other areas of  the  device  will
			  return  blocks  of  zeros.   Virtual  snapshot is implemented by
			  creating a hidden virtual device of the requested size using the
			  zero target.  A suffix of _vorigin is used for this device.


*   **zero** (*optional*): whether to set zero of the  first  KB of data in the new LV, by default ***True***

		Note:
			  Volume will not be zeroed if read only flag is set.
			  Snapshot volumes are zeroed always.

*   **zero** (*optional*): whether to set zero of the  first  KB of data in the new LV, by default ***True***

		Note:
			  Volume will not be zeroed if read only flag is set.
			  Snapshot volumes are zeroed always.

*   **autobackup** (*optional*): whether to  metadata should be backed up automatically after a change, by default ***True***

		Note:
			You are strongly advised not to  disable  this! See vgcfgbackup(8)

*   **tag** (*optional*): add the tag to this VG 

		Note:
			A tag is a
			  word that can be used to group LVM2 objects  of  the  same  type
			  together.  Tags can be given on the command line in place of PV,
			  VG or LV arguments.  Tags should be prefixed  with  @  to  avoid
			  ambiguity.   Each  tag  is  expanded  by  replacing  it with all
			  objects possessing that tag which are of the  type  expected  by
			  its  position  on  the  command line.  PVs can only possess tags
			  while they are part of a Volume Group: PV tags are discarded  if
			  the  PV  is  removed  from the VG.  As an example, you could tag
			  some LVs as database and others as userdata  and  then  activate
			  the  database  ones  with  lvchange  -ay @database.  Objects can
			  possess  multiple  tags  simultaneously.   Only  the  new   LVM2
			  metadata   format  supports  tagging:  objects  using  the  LVM1
			  metadata format cannot be tagged because the on-disk format does
			  not support it.  Characters allowed in tags are: A-Z a-z 0-9 _ +
			  . - and as of version 2.02.78 the following characters are  also
			  accepted: / = ! : # &

*   **allocation policy** (*optional*): specify the allocation policy

		Example:
			contiguous,  cling,  normal, anywhere or inherit

		Note:
			When a command needs to allocate  Physical
			  Extents  from  the  Volume Group, the allocation policy controls
			  how they are chosen.  Each Volume Group and Logical  Volume  has
			  an allocation policy defined.  The default for a Volume Group is
			  normal which applies common-sense  rules  such  as  not  placing
			  parallel stripes on the same Physical Volume.  The default for a
			  Logical Volume is inherit which applies the same policy  as  for
			  the   Volume   Group.   These  policies  can  be  changed  using
			  lvchange(8) and vgchange(8) or overridden on the command line of
			  any  command  that  performs  allocation.  The contiguous policy
			  requires  that  new  Physical  Extents  be  placed  adjacent  to
			  existing Physical Extents.  The cling policy places new Physical
			  Extents on the same Physical Volume as existing Physical Extents
			  in  the  same  stripe  of  the  Logical  Volume.   If  there are
			  sufficient  free  Physical  Extents  to  satisfy  an  allocation
			  request  but  normal  doesn't  use them, anywhere will - even if
			  that reduces performance by placing  two  stripes  on  the  same
			  Physical Volume
					''',
					'cn'	:	''''''
				},
				'parameter'	:	{
					'path'		:	{
						'type'		:	'array',
						'required'	:	True,
						'visible'	:	True
					},
					'name'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'available'		:	{
						'type'		:	'line',
						'option'	:	['y', 'ay' , 'n', 'ey', 'en', 'ly', 'ln'],
						'required'	:	False,
					},
					'chunk size':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'contiguous':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
					},
					'discards':	{
						'type'		:	'line',
						'default'	:	'passdown',
						'option'	:	['ignore', 'nopassdown', 'passdown'],
						'required'	:	False,
					},
					'stripe number':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'stripe size':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'LE number':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'LE size':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'minor number':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'persistent':	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
					},
					'mirror number'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'no udev sync'	:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
					},
					'monitor'		:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False,
					},
					'ignore monitoring'	:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False,
					},
					'permission'	:	{
						'type'		:	'line',
						'option'	:	['r', 'rw'],
						'required'	:	False,
					},
					'permission'	:	{
						'type'		:	'line',
						'option'	:	['r', 'rw'],
						'required'	:	False,
					},
					'pool metadata size':	{
						'type'		:	'line',
						'required'	:	False,
					},
					'region size'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'readahead'	:	{
						'type'		:	'line',
						'option'	:	['ReadAheadSectors', 'auto', 'none'],
						'required'	:	False,
					},
					'snapshot'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'thinpool'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'type'		:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'type'		:	{
						'type'		:	'line',
						'option'	:	['raid1', 'raid4', 'raid5', 'raid6'],
						'required'	:	False,
					},
					'virtual size'	:	{
						'type'		:	'line',
						'required'	:	False,
					},
					'zero'			:	{
						'type'		:	'bool',
						'default'	:	True,
						'required'	:	False,
					},
					'tag'		:	{
						'type'		:	'line',
						'required'	:	False
					},
					'allocation policy'		:	{
						'type'		:	'line',
						'option'	:	['anywhere', 'contiguous', 'cling', 'inherit', 'normal'],
						'required'	:	False
					},
					'autobackup'		:	{
						'type'		:	'bool',
						'default'	:	False,
						'required'	:	False
					}
				}
			},
#			'ntp'	:	{},
#			'quota'	:	{},
#			'ssh'	:	{},
#			'raid'	:	{},
#			'iptables'	:	{}
		},
		'windows'	:	{}
	}

import json
a=json.dumps(attr())
with open('module.json', 'w+') as f:
	f.write(a)
 
