from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [

    {"id": 1, "título": "Shape of you", "artista": "Ed Sheeran", "Link": "https://www.youtube.com/watch?v=JGwWNGJdvx8&vl=en"},
    {"id": 2, "título": "Bring me to life", "artista": "Evanescence", "Link": "https://www.youtube.com/watch?v=3YxaaGgTQYM"},
    {"id": 3, "título": "Going Under", "artista": "Evanescence", "Link": "https://www.youtube.com/watch?v=CdhqVtpR2ts"},
    {"id": 4, "título": "In the end", "artista": "Linkin Park", "Link": "https://www.youtube.com/watch?v=eVTXPUF4Oz4"},
    {"id": 5, "título": "Numb", "artista": "Linkin Park", "Link": "https://www.youtube.com/watch?v=kXYiU_JCYtU"},
    {"id": 6, "título": "Faint", "artista": "Linkin Park", "Link": "https://www.youtube.com/watch?v=LYU-8IFcDPw"},

]

@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route("/musicas", methods= ["POST"])
def add_musica():
    nova_musica = request.json
    nova_musica["id"] = len(playlist) + 1
    playlist.append(nova_musica)
    return jsonify({"mensagem": "Nova música criada!", "musica": nova_musica}), 201

@app.route("/musicas/<int:id>")
def encontrar(id): 
    for musica in playlist:
        if id == musica["id"]:
            return musica

    return {"mensagem": "Música não encontrada"}, 404


app.run(debug=True, host="0.0.0.0")                         