import pytest
from src.domain.repository.contact_repository import ContactRepository
from src.domain.interactor.contact_interactor import ContactInteractor


def test_should_get_None_if_no_data(database):

    contact_repository = ContactRepository(None, database)
    interactor = ContactInteractor(None, contact_repository)

    contact = interactor.get_all_contacts()


def test_should_download_contacts_if_exist(database):

    contact_repository = ContactRepository(None, database)
    contact_interactor = ContactInteractor(None, contact_repository)
    all_contacts = contact_interactor.get_all_contacts()
    assert len(all_contacts) == 2
    assert all_contacts[0].id == "contact-id-1"
    assert all_contacts[0].name == "contact-name-1"
    assert all_contacts[0].e_mail == "contact-e-mail-1"
    assert all_contacts[0].observation == "contact-observation-1"
    

    assert all_contacts[1].id == "contact-id-2"
    assert all_contacts[1].name == "contact-name-2"
    assert all_contacts[1].e_mail == "contact-e-mail-2"
    assert all_contacts[1].observation == "contact-observation-2"
    


def test_should_get_contact_if_data(database):

    # Arrange

    contact_repository = ContactRepository(None, database)
    interactor = ContactInteractor(None, contact_repository)

    # Act

    contact_1 = interactor.get_contact_by_id("contact-id-1")
    contact_2 = interactor.get_contact_by_id("contact-id-2")

    # Assert

    assert contact_1.id == "contact-id-1"
    assert contact_1.name == "contact-name-1"
    assert contact_1.e_mail == "contact-e-mail-1"
    assert contact_1.observation == "contact-observation-1"
    

    assert contact_1.id == "contact-id-1"
    assert contact_1.name == "contact-name-1"
    assert contact_1.e_mail == "contact-e-mail-1"
    assert contact_1.observation == "contact-observation-1"
    
def test_update_contact_if_exists_if_not_post_it(database):
    
   contact_repository = ContactRepository(None, database)
   contact_interactor = ContactInteractor(None,contact_repository)

   data = {
        "id": "contact-1",
        "name": "unknowncontact",
        "e_mail": "unknowncontact",
        "observation": "unknowncontact",
    }
   contact_interactor.save_contact(data)

   contact =contact_interactor.get_contact_by_id("contact-1")

   assert contact.id == "contact-1"
   assert contact.name == "unknowncontact"
   assert contact.e_mail == "unknowncontact"
   assert contact.observation == "unknowncontact"
    
