# 視圖 - 直接面對使用者的使用者介面設計
from flask import Flask, request, jsonify, render_template

from app import app, db
from models import Record


@app.route("/")
def index():
    return render_template('index.html', title='To-Do List')


@app.route("/record", methods=['POST'])
def add_record():
    req_data = request.form
    todo = req_data['name']
    date = req_data['cost']
    record = Record(todo=todo, date=date)
    db.session.add(record)
    db.session.commit()
    return 'Create Succeeded', 200


@app.route("/record", methods=['GET'])
def get_records():
    records = Record.query.all()
    records_data = [
        {
            'id': record.id,
            'name': record.todo,
            'cost': record.date
        }
        for record in records
    ]
    return jsonify(records_data), 200


@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    record_data = {
        'id': record.id,
        'name': record.todo,
        'cost': record.date
    }
    return jsonify(record_data), 200


@app.route('/record/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    req_data = request.form
    record = Record.query.filter_by(id=record_id).first()
    record.todo = req_data['name']
    record.date = req_data['cost']
    db.session.add(record)
    db.session.commit()
    return 'Update Succeeded', 200


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    db.session.delete(record)
    db.session.commit()
    return 'Delete Succeeded', 200
