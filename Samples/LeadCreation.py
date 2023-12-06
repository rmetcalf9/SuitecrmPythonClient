
def exec(client, login_session):

    lead_module = client.getModules(login_session)["Leads"]


    print("\nGetting fields...")
    print(lead_module.getFields(login_session))

    print("\nCreating lead...")
    attributes = {
        "first_name": "Test",
        "last_name": "TerryALL",
        "title": "Job title todo",
        "email1": "terry@terrible.com",
        "phone_work": "+447714916071",
        "description": "Created by simple_test.py",
        "lead_source": "Conference",
        "lead_source_description": "Some place",
        "status": "New",
        "status_description": "Investor, Landlord, Looking for property"
    }
    lead_record = lead_module.createRecord(login_session, attributes)

    attributes["last_name"] = "TerryInvestor"
    attributes["status_description"] = "Investor"
    lead_record = lead_module.createRecord(login_session, attributes)
    attributes["last_name"] = "TerryLandlord"
    attributes["status_description"] = "Landlord"
    lead_record = lead_module.createRecord(login_session, attributes)
    attributes["last_name"] = "TerryLooking"
    attributes["status_description"] = "Looking for property"
    lead_record = lead_module.createRecord(login_session, attributes)

    #print("lead_record", lead_record)
    #
    # #lead_id = lead_record.getId()
    # lead_id = "7cb072c4-c320-f8f7-e375-65704a8625ec"
    #
    # print("\nQuierying lead by id...")
    # retrieved_lead_record = lead_module.getRecordById(login_session, id=lead_id)
    # print("retrieved_lead_record", retrieved_lead_record)

