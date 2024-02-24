# set up your client SSH configuration file so that you can connect
# to a server without typing a password.

file { '/home/.ssh/config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0600',
    content => "Host *\n    IdentityFile /home/.ssh/school\n    PasswordAuthentication no\n    PubkeyAuthentication yes\n",
}
