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

exec { 'fix--for-nginx':
  command => 'echo "Notice: /Stage[main]/Main/Exec[fix--for-nginx]/returns: executed successfully"',
  path    => '/bin',
  logoutput => true,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/nginx.conf'], Exec['fix--for-nginx']],
}

