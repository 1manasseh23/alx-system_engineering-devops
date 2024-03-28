#!/usr/bin/env bash
# Install Nginx package

package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
class { 'nginx':
  listen_port => 80,
}

# Create a custom 404 page
file { '/var/www/html/error404.html':
  ensure  => present,
  content => '<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>Ceci n\'est pas une page</h1>
    <p>Sorry, the requested page could not be found.</p>
</body>
</html>',
}

# Set up the default server block
nginx::resource::server { 'default':
  listen_port => 80,
  server_name => '_',
  location    => {
    '/' => {
      try_files => '$uri $uri/ /error404.html', # Custom 404 page
    },
  },
  error_page  => '404 /error404.html', # 301 redirect for /redirect_me
}
