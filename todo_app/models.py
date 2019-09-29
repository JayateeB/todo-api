from todo_app import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    done = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return f"Task: {self.title}"

    def to_json(self):
        return {
            "task id":self.id,
            "title": self.title,
            "done":self.done
        }

