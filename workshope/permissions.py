def check_permissionz(user):
    permissions = {}
    permissions['acces_granted'] = True

    try:
        if user.permissions == 'admin':
            permissions['acces_granted'] = True

        if user.permissions == 'staff':
            permissions['acces_granted'] = False

        
    except:
        pass

    return permissions