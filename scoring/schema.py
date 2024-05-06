"""
When creating a Competition:
    Create Competitor objects, and add them to a list
    Create Field objects, and add them to a list
    Create the Competition with the two lists

On a new scorer:
    Get the name
    Call Competition.add_scorer(scorer_name)

"""


class Field:
    def __init__(self, name: str, max_value: int) -> None:
        self.name = name
        self.max_value = max_value

    def __eq__(self, other: object) -> bool:
        if not hasattr(other, "name"):
            return False
        return other.name == self.name  # type: ignore

    def __hash__(self) -> int:
        return hash(self.name)


class Competitor:
    def __init__(self, name: str, index: int) -> None:
        self.name = name
        self.index = index
        # dict[scorer_name, dict[Field, value]]
        self.scores: dict[str, dict[Field, int | None]] = {}

    def score(self, scorer_name: str, field: Field, score: int):
        self.scores[scorer_name][field] = score


class Competition:
    def __init__(
            self,
            fields: list[Field],
            competitors: list[Competitor],
            scorers: list[str] | None = None,
    ) -> None:

        self.fields = fields
        self.competitors = competitors
        self.scorers = scorers if scorers else []
        self.current_competitor_index = 0

    def add_scorer(self, name: str):
        if name in self.scorers:
            return

        self.scorers.append(name)
        for competitor in self.competitors:
            competitor.scores[name] = {field: None for field in self.fields}

    def remove_scorer(self, name: str):
        if name not in self.scorers:
            return
        
        self.scorers.remove(name)
        for competitor in self.competitors:
            competitor.scores.pop(name)

    def score(self, scorer_name: str, competitor_index: int, field: Field, value: int):
        self.competitors[competitor_index].score(scorer_name, field, value)


competition: Competition | None = None


def get_competition() -> Competition | None:
    global competition
    return competition


def new_competition(
    fields: list[Field],
    competitors: list[Competitor],
    scorers: list[str] | None = None,
) -> Competition:
    global competition
    competition = Competition(fields, competitors, scorers)
    return competition


def delete_competition():
    global competition
    competition = None
