from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan
import api.permission_handler as permission_handler
import api.email_handler as email_handler

# initialize the event structure
# if i comment away email_handler, there will be no email sent out
permission_handler.setup_permission_event_handlers()
email_handler.setup_permission_event_handlers()

if __name__ == "__main__":
    register_new_user("tom", "securepassword", "x@x.com")
    password_forgotten("x@x.com")
    upgrade_plan("x@x.com")
