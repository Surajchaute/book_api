from flask import jsonify, request
from bkconfig import app, db
from bmodels import Bookstore

@app.route('/book/api', methods=['GET'])
def Bookstore_list():
    bookstore_list = Bookstore.query.all()
    return jsonify(
        [{"BOOKSTORE_ID": book.id,
          "BOOK_TITLE": book.title,
          "BOOKSTORE_AUTHOR": book.author,
          "BOOKSTORE_PUBLISHED_DATE": book.published_date}
         for book in bookstore_list])

@app.route('/book/api', methods=['POST'])
def Bookstore_Add():
    try:
        reqdata = request.get_json()
        if not reqdata:
            return jsonify({"ERROR": "No data provided"}), 400

        book = Bookstore(
            title=reqdata.get("BOOK_TITLE"),
            author=reqdata.get("BOOKSTORE_AUTHOR"),
            published_date=reqdata.get("BOOKSTORE_PUBLISHED_DATE")
        )
        db.session.add(book)
        db.session.commit()
        return jsonify({"SUCCESS": f"New Book Added {book.id} Successfully "})
    except Exception as e:
        return jsonify({"ERROR": str(e)}), 500

@app.route('/book/api/<int:bid>', methods=['DELETE'])
def Bookstore_delete(bid):
    if bid <= 0:
        return jsonify({"ERROR": "Invalid ID"}), 400

    record = Bookstore.query.filter_by(id=bid).first()
    if not record:
        return jsonify({"ERROR": "No Book Record with Given ID for Delete"}), 404

    db.session.delete(record)
    db.session.commit()
    return jsonify({"SUCCESS": "Book removed Successfully!"})

@app.route('/book/api/<int:bid>', methods=['PUT'])
def Bookstore_update(bid):
    record = Bookstore.query.filter_by(id=bid).first()
    if not record:
        return jsonify({"ERROR": "No Book Record with Given ID for Update"}), 404

    reqdata = request.get_json()
    if not reqdata:
        return jsonify({"ERROR": "No data provided"}), 400

    record.title = reqdata.get("BOOK_TITLE", record.title)
    record.author = reqdata.get("BOOKSTORE_AUTHOR", record.author)
    db.session.commit()
    return jsonify({"SUCCESS": "Bookstore record Updated Successfully!"})

@app.route('/book/api/<int:bid>', methods=['GET'])
def Bookstore_search(bid):
    book = Bookstore.query.filter_by(id=bid).first()
    if not book:
        return jsonify({"ERROR": "No Book Record with Given ID for Search"}), 404

    return jsonify({"BOOKSTORE_ID": book.id,
                    "BOOK_TITLE": book.title,
                    "BOOKSTORE_AUTHOR": book.author,
                    "BOOKSTORE_PUBLISHED_DATE": book.published_date})





if __name__ == "__main__":
    app.run(debug=True)



