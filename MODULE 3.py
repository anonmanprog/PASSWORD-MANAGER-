def list_applications():
    if passwords_db:
        return list(passwords_db.keys())
    return "No applications stored yet." 
