from repo.contacts import ContactRepo
from schemas.contact import Contact, ContactCreate, ContactUpdate
from models.contact import ContactDB
from sqlalchemy.orm import Session

class ContactService():
    def __init__(self, db) -> None:
        self.repo = ContactRepo(db=db)

    def get_all_contacts(self) -> list[Contact]:
        all_contacts_from_db = self.repo.get_all()
        result = [Contact.from_orm(item) for item in all_contacts_from_db]
        return result
    
    def create_new(self, create_item: ContactCreate) -> Contact:
        new_item_from_db = self.repo.create(create_item)
        return Contact.from_orm(new_item_from_db)
    
    def get_by_id(self, id: int) -> Contact:
        contact_item = self.repo.get_by_id(id)
        return Contact.from_orm(contact_item)
    
    def update_contact(self, id: int, contact_update: ContactUpdate) -> Contact:
        update_item = self.repo.update_by_id(id, contact_update)
        return Contact.from_orm(update_item)
    
    def delete_contact(self, contact_id):
        return self.repo.delete_by_id(contact_id)
    
    def search_contacts(self, query: str) -> list[Contact]:
        return self.repo.search_contacts(query)
    
    def upcoming_birthdays(self) -> list[Contact]:
        return self.repo.get_upcoming_birthdays()
