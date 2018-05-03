from app import db, ma


class User(db.Model):
    # Main pattern
    id = db.Column(db.Integer, primary_key=True)
    reference_code = db.Column(db.String(100), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime,  nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Custom fields
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    username = db.Column(db.String(100), index=True, unique=True, nullable=True)
    token = db.Column(db.String(150), index=False, unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
