# installing flask from  pip3 using puppet

package { 'python3-pip':
    ensure => 'installed',
}

exec { 'install_flask':
    command => 'pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/usr/local/bin'],
    require => Package['python3-pip'],
    unless  => 'pip3 show flask | grep Version | grep 2.1.0',
}
