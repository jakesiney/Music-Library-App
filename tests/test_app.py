from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "An Album",
        "Another Album",
    ])
    expect(paragraph_tags).to_have_text([
        "Released: 2023",
        "Released: 1999"
    ])


def test_get_album_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_app.sql")
    page.goto(f"http://{test_web_address}/album/1")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text = 'An Album'
    expect(paragraph_tags).to_have_text = 'Released: 2023'


def test_get_album_by_id_two(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_app.sql")
    page.goto(f"http://{test_web_address}/album/2")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text = 'Another Album'
    expect(paragraph_tags).to_have_text = 'Released: 1999'


# === Example Code Below ===
"""
We can get an emoji from the /emoji page
"""


def test_get_emoji(page, test_web_address):  # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
