# kill process

exec { 'pkill':
    command  => 'pkill -f killmenow',
    provider => 'shell',
    creates  => '/killmenow',
    path     => ['/sbin', '/bin', '/usr/bin', '/usr/sbin']
}