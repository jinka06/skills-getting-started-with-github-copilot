def test_root_redirect(client):
    """
    Arrange: Prepare test client
    Act: Make GET request to root
    Assert: Verify redirect response
    """
    # Arrange - setup is done by client fixture

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
