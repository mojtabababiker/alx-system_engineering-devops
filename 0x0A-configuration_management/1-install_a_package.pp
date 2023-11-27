# install flask from pip3 using puppet

package {'werkzeug':
  ensure   => '2.1.1',
  name     => 'Werkzeug',
  provider => pip3
  }

package {'Flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider => pip3,
  require  => Package['werkzeug']
  }
