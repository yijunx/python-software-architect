from api.event import subscribe
import util.permission as permissionService


def handle_user_register_event(user):
    permissionService.add_permission(user.name)


def setup_permission_event_handlers():
    subscribe("USER_REGISTER", handle_user_register_event)
