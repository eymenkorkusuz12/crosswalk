{
  'sources': [
    'common/binding_object.h',
    'common/binding_object_store.cc',
    'common/binding_object_store.h',
    'common/common.idl',
    'common/event_target.cc',
    'common/event_target.h',
    'raw_socket/raw_socket.idl',
    'raw_socket/raw_socket_api.js',
    'raw_socket/raw_socket_extension.cc',
    'raw_socket/raw_socket_extension.h',
    'raw_socket/raw_socket_object.cc',
    'raw_socket/raw_socket_object.h',
    'raw_socket/tcp_socket.idl',
    'raw_socket/tcp_socket_object.cc',
    'raw_socket/tcp_socket_object.h',
  ],
  'dependencies': [
    'sysapps/sysapps_resources.gyp:xwalk_sysapps_resources',
  ],
}
