from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
api = Api(app)


class ContactsBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'phone_number': self.phone_number,
        }


parser = reqparse.RequestParser(bundle_errors=True)


class Todo(Resource):
    def get(self, contact_id):
        return jsonify(ContactsBook.serialize(
            ContactsBook.query.filter_by(id=contact_id)
                .first_or_404(description='Record with id={} is not available'.format(contact_id))))

    def delete(self, contact_id):
        record = ContactsBook.query.filter_by(id=contact_id) \
            .first_or_404(description='Record with id={} is not available'.format(contact_id))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, contact_id):
        data = request.json
        record = ContactsBook.query.filter_by(id=contact_id) \
            .first_or_404(description='Record with id={} is not available'.format(contact_id))
        record.name = data['name']
        record.second_name = data.get('second_name')
        record.phone_number = data.get('phone_number')
        db.session.commit()
        return ContactsBook.serialize(record), 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        records = ContactsBook.query.all()
        return jsonify([ContactsBook.serialize(record) for record in records])

    def post(self):
        data = request.json
        contact = ContactsBook(
            name=data['name'],
            second_name=data.get('second_name'),
            phone_number=data.get('phone_number')
        )
        db.session.add(contact)
        db.session.commit()
        return ContactsBook.serialize(contact), 201


api.add_resource(TodoList, '/contacts')
api.add_resource(Todo, '/contacts/<contact_id>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
