# turn off pass and declare identity file

File_line { 'passwd auth':
          path    => '/etc/ssh/ssh_config',
          line    => 'PasswordAuthentication no',
}

File_line { 'identity file':
          path       => '/etc/ssh/ssh_config',
          line       => 'IdentityFile ~/.ssh/holberton',
}