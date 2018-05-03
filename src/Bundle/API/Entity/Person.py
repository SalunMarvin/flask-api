from app import db, ma
from .User import User, UserSchema


class Person(db.Model):
    # Main pattern
    id = db.Column(db.Integer, primary_key=True)
    reference_code = db.Column(db.String(100), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime,  nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Custom fields
    name = db.Column(db.String(255), index=True, unique=True, nullable=True)
    document_number = db.Column(db.String(100), index=True, unique=True, nullable=True)
    kind = db.Column(db.String(100), index=False, unique=True, nullable=True)
    avatar = db.Column(db.String(255), index=False, unique=True, nullable=True)

    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='person')

    def __repr__(self):
        return '<Person %r>' % self.username


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
