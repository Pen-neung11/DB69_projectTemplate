# ============================================================
#  app.py — เว็บแอป Flask (ทำให้เสร็จแล้ว ★ ไม่ต้องแก้)
#  รัน:  python app.py  แล้วเปิด http://127.0.0.1:5000
# ============================================================
from flask import Flask, request, jsonify, render_template
import db

app = Flask(__name__)


def safe(fn, *args, **kwargs):
    try:
        return jsonify({"ok": True, "data": fn(*args, **kwargs)})
    except NotImplementedError as e:
        return jsonify({"ok": False, "todo": True, "error": str(e)}), 501
    except Exception as e:
        return jsonify({"ok": False, "error": f"{type(e).__name__}: {e}"}), 500


@app.route("/")
def page_home():
    return render_template("index.html")

@app.route("/report")
def page_report():
    return render_template("report.html")


# ---- ผู้เรียน ----
@app.route("/api/learners", methods=["GET"])
def learners_list():
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_learners, filters)

@app.route("/api/learners/<int:_id>", methods=["GET"])
def learner_get(_id):
    return safe(db.get_learner, _id)

@app.route("/api/learners", methods=["POST"])
def learner_create():
    return safe(db.create_learner, request.json)

@app.route("/api/learners/<int:_id>", methods=["PUT"])
def learner_update(_id):
    return safe(db.update_learner, _id, request.json)

@app.route("/api/learners/<int:_id>", methods=["DELETE"])
def learner_delete(_id):
    return safe(db.delete_learner, _id)

# ---- คอร์ส ----
@app.route("/api/courses", methods=["GET"])
def courses_list():
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_courses, filters)

@app.route("/api/courses/<int:_id>", methods=["GET"])
def course_get(_id):
    return safe(db.get_course, _id)

@app.route("/api/courses", methods=["POST"])
def course_create():
    return safe(db.create_course, request.json)

@app.route("/api/courses/<int:_id>", methods=["PUT"])
def course_update(_id):
    return safe(db.update_course, _id, request.json)

@app.route("/api/courses/<int:_id>", methods=["DELETE"])
def course_delete(_id):
    return safe(db.delete_course, _id)

# ---- การลงทะเบียน ----
@app.route("/api/enrollments", methods=["GET"])
def enrollments_list():
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_enrollments, filters)

@app.route("/api/enrollments/<int:_id>", methods=["GET"])
def enrollment_get(_id):
    return safe(db.get_enrollment, _id)

@app.route("/api/enrollments", methods=["POST"])
def enrollment_create():
    return safe(db.create_enrollment, request.json)

@app.route("/api/enrollments/<int:_id>", methods=["PUT"])
def enrollment_update(_id):
    return safe(db.update_enrollment, _id, request.json)

@app.route("/api/enrollments/<int:_id>", methods=["DELETE"])
def enrollment_delete(_id):
    return safe(db.delete_enrollment, _id)


@app.route("/api/reports/summary")
def report_summary():
    return safe(db.report_summary)

@app.route("/api/reports/popular-courses")
def route_report_popular_courses():
    return safe(db.report_popular_courses)

@app.route("/api/reports/completion-rate")
def route_report_completion_rate():
    return safe(db.report_completion_rate)

@app.route("/api/reports/prerequisites")
def route_report_course_prerequisites():
    return safe(db.report_course_prerequisites)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
