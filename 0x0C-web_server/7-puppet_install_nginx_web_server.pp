#!/usr/bin/puppet apply
# install and configure an Nginx server using puppet

#variables
$config = "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}"

#updating the package manager
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

#installing the Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}

#configuring the Nginx server
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $config,
}

#starting the Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => 'true',
  require   => Package['nginx'],
  subscribe => [File['/var/www/html/index.html'], File['/var/www/html/404.html'],
  File['/etc/nginx/sites-available/default']],
}