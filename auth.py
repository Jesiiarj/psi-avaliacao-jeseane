from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)

@auth.py("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("registro"))
    hashed_password = generate_password_hash(senha)
    usuario_db[email] = {"senha": hashed_password}

    return render_template("registro.html")



@auth.py("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("login"))

    return render_template("login.html")


@auth_.py("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))


@auth_bp.route("/registro", methods=["POST"])
def registro():
    if request.method==(POST)():
    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return ({"error": "E-mail e senha são obrigatórios"}), 404

    if email in usuario_db:
        return ({"error": "Usuário já cadastrado"}), 400
    session["usuario_id"];

    return ({"message": "Usuário registrado"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = users_db.get(email)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=email)
    return ({"token": access_token}), 200


@app.route("/me", methods=["GET"])
@jwt_required()  
def get_profile():

    current_user_email = get_jwt_identity()
    return ({"logged_in_as": current_user_email, "status": "Acesso autorizado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;app.register-bp(auth)
# - a rota /logout.
