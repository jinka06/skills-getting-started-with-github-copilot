def test_unregister_success(client, reset_activities):
    """
    Arrange: Prepare test client with existing participant
    Act: Delete participant from activity
    Assert: Verify participant is removed
    """
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert f"Removed {email} from {activity}" in response.json()["message"]


def test_unregister_nonexistent_participant(client, reset_activities):
    """
    Arrange: Prepare test client with non-existent participant
    Act: Try to delete non-existent participant
    Assert: Verify 404 response
    """
    # Arrange
    email = "nonexistent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_unregister_invalid_activity(client, reset_activities):
    """
    Arrange: Prepare test client with non-existent activity
    Act: Try to delete from non-existent activity
    Assert: Verify 404 response
    """
    # Arrange
    email = "student@mergington.edu"
    activity = "NonExistent Club"

    # Act
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_unregister_verifies_removal(client, reset_activities):
    """
    Arrange: Prepare test client with existing participant
    Act: Delete participant and verify via GET
    Assert: Verify participant is no longer in list
    """
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act - Delete the participant
    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email}
    )

    # Assert - Verify deletion was successful
    assert response.status_code == 200

    # Act - Fetch activities to verify removal
    response = client.get("/activities")
    activities_data = response.json()

    # Assert - Verify participant is no longer in the list
    assert email not in activities_data[activity]["participants"]
    assert "daniel@mergington.edu" in activities_data[activity]["participants"]
