#!/usr/bin/env python
__author__ = 'igis_gzy'

# server_controller = functools.partial(_create_controller,
#     servers.ServersController,
#     [
#         config_drive.ConfigDriveController,
#         extended_availability_zone.ExtendedAZController,
#         extended_server_attributes.ExtendedServerAttributesController,
#         extended_status.ExtendedStatusController,
#         extended_volumes.ExtendedVolumesController,
#         hide_server_addresses.Controller,
#         keypairs.Controller,
#         security_groups.SecurityGroupsOutputController,
#         server_usage.ServerUsageController,
#     ],
#     [
#         admin_actions.AdminActionsController,
#         admin_password.AdminPasswordController,
#         console_output.ConsoleOutputController,
#         create_backup.CreateBackupController,
#         deferred_delete.DeferredDeleteController,
#         evacuate.EvacuateController,
#         floating_ips.FloatingIPActionController,
#         lock_server.LockServerController,
#         migrate_server.MigrateServerController,
#         multinic.MultinicController,
#         pause_server.PauseServerController,
#         remote_consoles.RemoteConsolesController,
#         rescue.RescueController,
#         security_groups.SecurityGroupActionController,
#         shelve.ShelveController,
#         suspend_server.SuspendServerController
#     ]
# )

# server_controller = functools.partial(_create_controller,
#     servers.ServersController,
#     [
#         "abcadgf",
#         544312
#     ],
#     [
#         123456
#     ]
# )

server_controller = "sadfasdfasfd"

ROUTE_LIST = (
    ('/servers', {
        'GET': [server_controller, 'index'],
        'POST': [server_controller, 'create']
    }),
    ('/servers/detail', {
        'GET': [server_controller, 'detail']
    }),
    ('/servers/{id}', {
        'GET': [server_controller, 'show'],
        'PUT': [server_controller, 'update'],
        'DELETE': [server_controller, 'delete']
    }),
    ('/servers/{id}/action', {
        'POST': [server_controller, 'action']
    })
)

def test():
    for path, methods in ROUTE_LIST:
        for method, controller_info in methods.items():
            # controller = controller_info[0]()
            action = controller_info[1]
            # print controller,action
            print action

if __name__ == "__main__":
    test()

