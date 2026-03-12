def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_status_code = 200
    required_activity_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == expected_status_code
    assert isinstance(payload, dict)
    assert payload

    first_activity = next(iter(payload.values()))
    assert required_activity_keys.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)
