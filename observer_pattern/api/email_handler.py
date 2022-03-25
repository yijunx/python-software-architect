from api.event import subscribe
import util.email as emailService


def handle_user_register_event(user):
    emailService.send_email(email=user.email, title="aaa")


def setup_permission_event_handlers():
    subscribe("USER_REGISTER", handle_user_register_event)