from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        nome = (request.form.get("nome") or "").strip()
        senha = request.form.get("senha") or ""

        if database.buscar_usuario_por_email(email):
            flash("E-mail já cadastrado.")
            return redirect(url_for("auth.registro"))

        if not nome or not email or not senha:
                    flash("Preencha nome, e-mail e senha.")
                    return redirect(url_for("auth.registro"))
        
    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        senha = request.form.get("senha") or ""

        usuario = database.buscar_usuario_por_email(email)
        if not usuario or not check_password_hash(usuario.senha_hash, senha):
            flash("Credenciais inválidas.")
            return redirect(url_for("auth.login"))

        if not email or not senha:
            flash("Informe e-mail e senha.")
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
