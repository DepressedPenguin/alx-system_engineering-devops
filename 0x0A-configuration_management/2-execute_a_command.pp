# create a manifest kill pro

exec { 'pkill':
command  => 'pkill killmenow',
provider => 'shell'
}
