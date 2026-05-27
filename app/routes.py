from flask import Blueprint, jsonify
from app.models import Candidate, db

candidates_bp = Blueprint("candidates", __name__)


@candidates_bp.route("/api/candidates/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    candidate = db.session.get(Candidate, candidate_id)

    if candidate is None:
        return jsonify({"error": "candidate not found"}), 404

    return (
        jsonify(
            {
                "id": candidate.id,
                "name": candidate.name,
                "email": candidate.email,
            }
        ),
        200,
    )
