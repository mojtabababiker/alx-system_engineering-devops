# Kill a process using puppet exec resource

exec { 'Killmenow':
  command => '/usr/bin/pkill killmenow',
  }
