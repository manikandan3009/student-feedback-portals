
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for demo purposes (resets on server restart)
FEEDBACKS = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        course = request.form.get("course", "").strip()
        rating = request.form.get("rating", "").strip()
        comments = request.form.get("comments", "").strip()

        if course and rating:
            FEEDBACKS.append({
                "course": course,
                "rating": int(rating),
                "comments": comments
            })
            return redirect(url_for("thanks"))
    return render_template("index.html")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


@app.route("/admin")
def admin():
    return render_template("admin.html", feedbacks=FEEDBACKS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
