def test_index_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Student Feedback Portal" in resp.data


def test_submit_feedback_redirects_to_thanks(client):
    resp = client.post('/', data={
        'course': 'CS101',
        'rating': '5',
        'comments': 'Great!'
    }, follow_redirects=False)
    assert resp.status_code in (302, 303)
    assert resp.headers.get('Location', '').endswith('/thanks')
