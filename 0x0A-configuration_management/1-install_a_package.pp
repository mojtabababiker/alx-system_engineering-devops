# install flask from pip3 using puppet

package {'Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => pip3
  }
