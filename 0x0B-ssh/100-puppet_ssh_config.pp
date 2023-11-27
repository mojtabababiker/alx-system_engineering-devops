# Edit the SSh client configuration file to use ~/.ssh/school private key and
# without password login

$content = "Include /etc/ssh/ssh_config.d/*.conf
Host *
     PasswordAuthentication no
     IdentityFile ~/.ssh/school
     SendEnv LANG LC_*
     HashKnownHosts yes
     GSSAPIAuthentication yes"

file { 'client_auth':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => $content
}