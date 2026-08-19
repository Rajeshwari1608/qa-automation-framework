def test_insert_and_read_user(database):

    database.execute_update(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Rajeshwari", "rajeshwari@example.com")
    )

    users = database.execute_query(
        "SELECT name, email FROM users WHERE name = ?",
        ("Rajeshwari",)
    )

    assert len(users) == 1
    assert users[0][0] == "Rajeshwari"
    assert users[0][1] == "rajeshwari@example.com"

def test_update_user(database):

    database.execute_update(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Rajeshwari", "old@example.com")
    )

    database.execute_update(
        "UPDATE users SET email = ? WHERE name = ?",
        ("new@example.com", "Rajeshwari")
    )

    users = database.execute_query(
        "SELECT email FROM users WHERE name = ?",
        ("Rajeshwari",)
    )

    assert users[0][0] == "new@example.com"

def test_delete_user(database):

    database.execute_update(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Rajeshwari", "rajeshwari@example.com")
    )

    database.execute_update(
        "DELETE FROM users WHERE name = ?",
        ("Rajeshwari",)
    )

    users = database.execute_query(
        "SELECT * FROM users WHERE name = ?",
        ("Rajeshwari",)
    )

    assert len(users) == 0