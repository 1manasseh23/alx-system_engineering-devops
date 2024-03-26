#!/usr/bin/env bash
#  we’d like you to set up your client SSH configuration file
# so that you can connect to a server without typing a password.

file_line { 'Turn off passwd auth':
  ensure            => present,
  path              => '/etc/ssh/sshd_config',
  line              => 'PasswordAuthentication no',
  match             => '^PasswordAuthentication',
}

file_line { 'Declare identity file':
  ensure            => present,
  path              => '/etc/ssh/sshd_config',
  line              => 'IdentityFile ~/.ssh/school',
  match             => '^#?IdentityFile',
}
