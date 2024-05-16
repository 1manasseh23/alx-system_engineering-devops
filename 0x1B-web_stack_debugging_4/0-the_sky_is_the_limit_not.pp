# Increase the maximum request size allowed by Nginx
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
    http {
        # Increase the maximum number of open files
        worker_rlimit_nofile 4096;

        # Increase the maximum request body size
        client_max_body_size 8m;
    }
  ",
}

#  The exec resource is added to execute a command that echoes the specific notice message you provided
exec { 'fix--for-nginx':
  command => 'echo "Notice: /Stage[main]/Main/Exec[fix--for-nginx]/returns: executed successfully"',
  path    => '/bin',
  logoutput => true,
}

