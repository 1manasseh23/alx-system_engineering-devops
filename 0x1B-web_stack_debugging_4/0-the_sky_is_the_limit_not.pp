# Increase the ULIMIT of nginx default
exec { 'fix--for-nginx':
        # Increase the ULIMIT
        command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
        # Specify the path to nginx file
        path    => '/usr/local/bin/:/bin/',
}

# Restart nginx
exec { 'nginx-restart':
        # Restart nginx service
        command => '/etc/init.d/nginx restart',
        # the path init to restart
        path    => '/etc/init.d/',
}

