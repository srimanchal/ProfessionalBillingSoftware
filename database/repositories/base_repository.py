from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self):
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def get_by_id(self, model, entity_id):
        return self.session.get(model, entity_id)

    def get_all(self, model):
        return self.session.query(model).all()