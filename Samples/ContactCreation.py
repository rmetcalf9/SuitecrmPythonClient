

def exec(client, login_session):

    contact_module = client.getModules(login_session)["Contacts"]
    print("\nGetting fields...")
    print(contact_module.getFields(login_session))

    print("\nCreating contact...")
    attributes = {
        "first_name": "Test",
        "last_name": "Contact",
        "title": "Job title todo",
        "email1": "rmetcalf9+testcrm@googlemail.com",
        "phone_work": "+447714916071",
        "description": "WHERE DID WE MEET\n\nCreated by simple_test.py",
        "lead_source": "Conference"
    }
    contact_record = contact_module.createRecord(login_session, attributes)
