def test_signup_success(client, reset_activities):
    """
    Arrange: Prepare test client and test data
    Act: Post signup request for new participant
    Assert: Verify participant is added to activity
    """
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Basketball Team"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json()["message"]


def test_signup_duplicate_email(client, reset_activities):
    """
    Arrange: Prepare test client with existing participant
    Act: Try to signup same email twice
    Assert: Verify second signup is rejected with 400
    """
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_invalid_activity(client, reset_activities):
    """
    Arrange: Prepare test client and non-existent activity
    Act: Try to signup for non-existent activity
    Assert: Verify 404 response
    """
    # Arrange
    email = "student@mergington.edu"
    activity = "NonExistent Club"

    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_signup_multiple_activities(client, reset_activities):
    """
    Arrange: Prepare test client and test data
    Act: Signup same student for multiple activities
    Assert: Verify student is added to multiple activities
    """
    # Arrange
    email = "alice@mergington.edu"
    activities_to_join = ["Art Club", "Drama Club"]

    # Act & Assert
    for activity in activities_to_join:
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        assert response.status_code == 200

    # Verify both signups worked
    response = client.get("/activities")
    activities_data = response.json()
    assert email in activities_data["Art Club"]["participants"]
    assert email in activities_data["Drama Club"]["participants"]
