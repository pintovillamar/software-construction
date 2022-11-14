from database import db, ma
from flask import Flask

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f"test('{self.name}', '{self.description}')"
    
class testSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "description"
        )
    
test_schema = testSchema()
tests_schema = testSchema(many=True)

class testModel:
    pass