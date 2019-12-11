# turn off pass and declare identity file

file_line { 'passwd auth':
          path    => '/etc/ssh/ssh_config',
          line    => 'PasswordAuthentication no',
}

file_line { 'identity file':
          path       => '/etc/ssh/ssh_config',
          line       => 'IdentityFile ~/.ssh/holberton',
}
