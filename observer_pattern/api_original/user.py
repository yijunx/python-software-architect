import util.email as emailService
import util.db_repo as dbService
import util.permission as permissionService


def register_new_user(name, password, email):
    """has weak cohesion, it needs to know a log of things
    and it does a lot of jobs, and this file has a lot
    of imports..."""

    print("########### REGISTER BEGINS #############")

    user = dbService.create_user(name, email, password)

    emailService.send_email(email=user.email, title="hey")

    permissionService.add_permission(user.name)

    print("########### REGISTER ENDS #############")


def password_forgotten(email):
    print("PASSWORD FORGOTTEN", email)

    print("SEND AN EMAIL BECAUSE YOU FORGET")
