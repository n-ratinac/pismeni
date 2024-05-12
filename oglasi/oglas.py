from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from .db import get_db
bp = Blueprint("oglas", __name__, url_prefix="/oglas")

@bp.route("/<int:id>", methods=["GET"])
def view(id):
    db = get_db()
    try:
        oglas = db.execute("SELECT * FROM oglas WHERE id = ?", (id,)).fetchone()
        kategorija = db.execute("SELECT naziv FROM kategorija WHERE id = ?", (oglas["kategorija_id"],)).fetchone()
    except:
        flash("Oglas ne postoji")
        return redirect(url_for("oglas.index"))
    
    return render_template("oglas/view.html", oglas=oglas, kategorija=kategorija['naziv'])

@bp.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    db = get_db()
    db.execute("DELETE FROM oglas WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("oglas.index"))

@bp.route("/kategorija/<int:id>", methods=["GET"])
def kategorija(id):
    db = get_db()
    oglasi = db.execute("SELECT * FROM oglas WHERE kategorija_id = ?", (id,)).fetchall()
    return render_template("oglas/index.html", oglasi=oglasi)