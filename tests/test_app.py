import pytest
import os
import app.app_logic as app_logic
import time

url = "https://www.yahoo.com/finance/news/collecting-degrees-thermometer-atlanta-woman-110000419.html"

@pytest.mark.skipif(not os.getenv('DATABASE_URL'), reason="Requires DATABASE_URL to run")
def test_create_page():
    page = app_logic.create_page(url)
    assert page != None

@pytest.mark.skipif(not os.getenv('DATABASE_URL'), reason="Requires DATABASE_URL to run")
async def test_bookmark_page():
    # Check if bookmark already exists, if yes delete it.
    # This makes the test more realistic.
    bookmark = app_logic.get_bookmark_by_url(url)
    if bookmark:
        app_logic.delete_bookmark_and_associate_records(bookmark.id)

    page = app_logic.create_page(url)
    bm = app_logic.create_bookmark(page)
    bookmark = app_logic.get_bookmark_by_url(url)
    assert bookmark is not None

    doc = app_logic.get_document_by_id(bookmark.document_id)
    assert doc.id is not None
    assert doc.url == url
    assert len(doc.original_text) > 0
    assert isinstance(doc.original_text, str)

    # Store the document id for future methods
    document_id = doc.id
    app_logic.extract_info_from_doc(doc)

    # Testing the retrieval of document from the database
    doc = None
    doc = app_logic.get_document_by_id(document_id)

    # Testing the LLM extraction worked
    assert doc is not None

@pytest.mark.skipif(not os.getenv('DATABASE_URL'), reason="Requires DATABASE_URL to run")
def test_get_concepts_by_document_id():
    bookmark = app_logic.get_bookmark_by_url(url)
    doc = app_logic.get_document_by_id(bookmark.document_id)
    concepts = app_logic.get_concepts_by_document_id(doc.id)
    assert len(concepts) > 0
    assert concepts[0].document_id == doc.id
    assert isinstance(concepts, list)

@pytest.mark.skipif(not os.getenv('DATABASE_URL'), reason="Requires DATABASE_URL to run")
def test_get_entities_by_document_id():
    bookmark = app_logic.get_bookmark_by_url(url)
    doc = app_logic.get_document_by_id(bookmark.document_id)
    entities = app_logic.get_entities_by_document_id(doc.id)
    assert len(entities) > 0
    assert entities[0].document_id == doc.id
    assert isinstance(entities, list)

