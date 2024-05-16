# Puppet manifest to configure the system for the holberton user

# Define the command to change the user's file descriptor limit
exec { 'change-os-configuration-for-holberton-user':
    command => '/bin/bash -c "echo \"holberton hard nofile 4096\" >> /etc/security/limits.conf && ulimit -n 4096"',
    path    => ['/bin', '/usr/bin'],
    unless  => '/bin/grep -q "holberton hard nofile 4096" /etc/security/limits.conf',
}

# Define a notify resource to print a message after the configuration is applied
notify { 'Holberton user configuration applied':
    require => Exec['change-os-configuration-for-holberton-user'],
}

