import functools

from flask import (
    Blueprint,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from scoring.schema import get_competition

bp = Blueprint('scorer', __name__, url_prefix='/')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None or get_competition() is None:
            return redirect(url_for('scorer.index'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    g.user = session.get('scorer_name')


@bp.route("/", methods=("GET", "POST"))
def index():
    error = ""
    if request.method == "POST":
        scorer_name = request.form.get("scorer-name")
        print(scorer_name)
        if scorer_name and scorer_name != "":
            session["scorer_name"] = scorer_name
            comp = get_competition()

            if comp is not None:
                comp.add_scorer(scorer_name)
                return redirect(url_for("scorer.view"))

            error += "The competition hasn't started yet."
        else:
            error += "Name was not found."

    flash(error, category=error)
    return render_template("scorer/index.jinja")


@bp.route("/view", methods=("GET",))
@login_required
def view():
    return render_template("scorer/view-all.jinja", competition=get_competition())


@bp.route("/view/<int:competitor_id>", methods=("GET", "POST"))
@login_required
def view_one(competitor_id: int):
    comp = get_competition()
    if comp is None or g.user is None:
        abort(402)

    current_competitor = comp.competitors[competitor_id]

    if request.method == "POST":
        for field_name in request.form:
            curr_field = None
            for field in comp.fields:
                if field.name == field_name:
                    curr_field = field
                    break
            else:
                abort(400)

            current_competitor.score(
                g.user,
                curr_field,
                int(request.form[field_name])
            )

    return render_template(
        "scorer/view-one.jinja",
        fields=current_competitor.scores[g.user],
        competitor = current_competitor)
