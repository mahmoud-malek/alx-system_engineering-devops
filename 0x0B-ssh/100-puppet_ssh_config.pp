# set up your client SSH configuration file so that you can connect
# to a server without typing a password.

file { '~/.ssh/school':
	ensure => present,
	content => "Host *\n PasswordAuthentication no\n PubkeyAuthentication yes\n IdentityFile ~/.ssh/school\n",
}
