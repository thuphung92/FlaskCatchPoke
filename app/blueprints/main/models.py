from app import db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    ability = db.Column(db.String(50))
    experience = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    sprite_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Pokemon ID: {self.id} | Name: {self.name}>'

    def save(self):
        db.session.add(self)
        db.session.commit()