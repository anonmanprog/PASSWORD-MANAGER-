def get_password(app):
    x = passwords_db.get(app)
    if x:
        return x
    return "No password found for '" + app + "'."



