# Edit the SSh client configuration file to use ~/.ssh/school private key and
# without password login

$content = "Include /etc/ssh/ssh_config.d/*.conf
    Host *
        PasswordAuthentication no
        SendEnv LANG LC_*
        HashKnownHosts yes
        GSSAPIAuthentication yes"

file { 'client_auth':
  path    => '/etc/ssh/ssh_config',
  ensure  => 'present',
  content => $content
}