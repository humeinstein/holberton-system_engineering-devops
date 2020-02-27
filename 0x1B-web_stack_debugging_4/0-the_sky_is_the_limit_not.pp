exec { 'fix-limit-in-bin':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
}
exec { 'nginx-refresh':         
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo service nginx restart',
}