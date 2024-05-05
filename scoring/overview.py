from flask import (
    Blueprint,
    render_template,
    request
)

from scoring.schema import (
    Competitor,
    Field,
    delete_competition,
    get_competition,
    new_competition
)

bp = Blueprint('overview', __name__, url_prefix='/overview')


@bp.route("/", methods=("GET",))
def index():
    return render_template("overview/index.jinja")


@bp.route("/create-competition", methods=("GET", "POST"))
def create_competition():
    if request.method == "GET":
        return render_template("overview/create-competition.jinja")

    # TODO: Fix this, my head hurts
    competitors = []
    fields = []
    for key in request.form:
        if request.form[key] == "":
            continue
        if "competitor" in key:
            competitors.append(Competitor(
                request.form[key],
                int(key[-1])-1,
            ))
        elif "field-name" in key:
            field_max_value = request.form["field-max"+key[-1]]
            if field_max_value == "":
                continue
            fields.append(Field(
                request.form[key],
                int(field_max_value),
            ))

    competition = new_competition(fields, competitors)

    return render_template("overview/index.jinja", competition=competition)


@bp.route("/delete-competition", methods=("POST",))
def delete_comp():
    delete_competition()
    return render_template("overview/index.jinja")


@bp.route("/competition", methods=("GET",))
def show_competition():

    return render_template("overview/show.jinja", competition=get_competition())
