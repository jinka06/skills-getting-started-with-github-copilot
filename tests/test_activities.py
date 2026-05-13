def test_get_all_activities(client, reset_activities):
    """
    Arrange: Prepare test client
    Act: Make GET request to /activities
    Assert: Verify all activities are returned with correct structure
    """
    # Arrange - setup is done by fixtures

    # Act
    response = client.get("/activities")
    activities_data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(activities_data, dict)
    assert len(activities_data) == 9
    assert "Chess Club" in activities_data
    assert "Programming Class" in activities_data


def test_activity_structure(client, reset_activities):
    """
    Arrange: Prepare test client
    Act: Make GET request to /activities
    Assert: Verify activity has required fields
    """
    # Arrange - setup is done by fixtures

    # Act
    response = client.get("/activities")
    activities_data = response.json()
    chess_club = activities_data["Chess Club"]

    # Assert
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_activity_participants_loaded(client, reset_activities):
    """
    Arrange: Prepare test client
    Act: Make GET request to /activities
    Assert: Verify participants are correctly loaded
    """
    # Arrange - setup is done by fixtures

    # Act
    response = client.get("/activities")
    activities_data = response.json()

    # Assert
    assert response.status_code == 200
    assert "michael@mergington.edu" in activities_data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in activities_data["Chess Club"]["participants"]
    assert len(activities_data["Chess Club"]["participants"]) == 2
