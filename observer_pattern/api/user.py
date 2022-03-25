import util.db_repo as dbService

from api.event import post_event


def register_new_user(name, password, email):
    """has weak cohesion, it needs to know a log of things
    and it does a lot of jobs, and this file has a lot
    of imports..."""

    print("########### REGISTER BEGINS #############")

    # this line remains because this is the what really 
    # required here..
    user = dbService.create_user(name, email, password)

    post_event("USER_REGISTER", user)


    # emailService.send_email(email=user.email, title="hey")

    # permissionService.add_permission(user.name)

    print("########### REGISTER ENDS #############")


def password_forgotten(email):
    print("PASSWORD FORGOTTEN", email)

    print("SEND AN EMAIL BECAUSE YOU FORGET")
