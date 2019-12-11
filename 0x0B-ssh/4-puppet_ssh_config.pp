# turn off pass and declare identity file

File_line { 'Turn off passwd auth':
          path    => '/etc/ssh/ssh_config',
          line    => 'PasswordAuthentication no',
	  }

File_line { 'Declare identity file':
          path       => '/etc/ssh/ssh_config',
          line       => 'IdentityFile ~/.ssh/holberton',
	  }
