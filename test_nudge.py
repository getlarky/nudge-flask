import os
import json
import pytest
from app import create_app, db


@pytest.fixture
def app():
    app = create_app(config_name="testing")
    with app.app_context():
        # create all tables
        db.create_all()
    yield app
    with app.app_context():
        # drop all tables
        db.session.remove()
        db.drop_all()

@pytest.fixture
def test_alert():
    return {'title': 'test', 'message': 'fun test!'}


class TestNudge(object):


    def test_alert_creation(self, app, test_alert):
        """Test API can create a bucketlist (POST request)"""
        res = app.test_client().post('/alerts/', data=test_alert)
        assert res.status_code == 201
        assert 'test' in str(res.data)

    def test_api_can_get_all_alerts(self, app, test_alert):
        """Test API can get a bucketlist (GET request)."""
        res = app.test_client().post('/alerts/', data=test_alert)
        assert res.status_code == 201
        res = app.test_client().get('/alerts/')
        assert res.status_code == 200
        assert 'test' in str(res.data)

    def test_api_can_get_bucketlist_by_id(self, app, test_alert):
        """Test API can get a single bucketlist by using it's id."""
        rv = app.test_client().post('/alerts/', data=test_alert)
        assert rv.status_code == 201
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = app.test_client().get(
            '/alerts/{}'.format(result_in_json['id']))
        assert result.status_code == 200
        assert 'test' in str(result.data)

    def test_alert_can_be_edited(self, app, test_alert):
        """Test API can edit an existing alert. (PUT request)"""
        rv = app.test_client().post(
            '/alerts/',
            data={'title': 'book idea', 'message': 'Eat, pray and love'})
        assert rv.status_code == 201
        rv = app.test_client().put(
            '/alerts/1',
            data={
                "message": "Dont just eat, but also pray and love :-)"
            })
        assert rv.status_code == 200
        results = app.test_client().get('/alerts/1')
        assert 'Dont just eat' in str(results.data)

    def test_edited_alert_must_have_title_and_message(self, app, test_alert):
        rv = app.test_client().post('/alerts/', data=test_alert)
        assert rv.status_code == 201
        rv = app.test_client().put(
            '/alerts/1',
            data={
                "message": "",
                "title": ""
            })
        assert rv.status_code == 500
        

    def test_alert_deletion(self, app, test_alert):
        """Test API can delete an existing alert. (DELETE request)."""
        rv = app.test_client().post(
            '/alerts/',
            data={'message': 'Eat, pray and love', 'title': 'movie idea'})
        assert rv.status_code == 201
        res = app.test_client().delete('/alerts/1')
        assert res.status_code == 200
        # Test to see if it exists, should return a 404
        result = app.test_client().get('/alerts/1')
        assert result.status_code == 404