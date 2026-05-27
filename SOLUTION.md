# Solution Steps

1. Open `app/routes.py` and update the `get_candidate()` view so it looks up the candidate by primary key and checks whether the result is `None` before building the success response.

2. If no candidate exists for the requested ID, return `jsonify({"error": "candidate not found"}), 404` so the API always responds with JSON instead of Flask’s default HTML 404 page.

3. If the candidate exists, return a JSON object containing only `id`, `name`, and `email`, along with HTTP status code `200`.

4. In `tests/test_candidates.py`, add a test for the seeded candidate. Use the `client` fixture to `GET /api/candidates/1`, then assert the status code is `200`, the response is JSON, and the parsed JSON matches the seeded candidate data.

5. Add a second test for a missing candidate. Request an ID that is not present, such as `/api/candidates/9999`, then assert the status code is `404`, the response is JSON, and the parsed JSON equals `{"error": "candidate not found"}`.

6. Run `pytest` and confirm both tests pass, verifying both the success path and the not-found JSON error behavior.

