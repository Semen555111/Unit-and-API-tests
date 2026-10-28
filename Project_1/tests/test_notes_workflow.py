import re
import pytest
from playwright.sync_api import expect
from Project_1.tests.pages.login_page import LoginPage
from Project_1.tests.pages.notes_page import NotesPage
from Project_1.tests.pages.register_page import RegisterPage


@pytest.mark.order(1)
def test_01_register_user_and_open_notes(notes_workflow):
    page = notes_workflow.page
    register_page = RegisterPage(page)
    register_page.open()
    register_page.register(
        "QA Student", notes_workflow.email, notes_workflow.password
    )
    expect(register_page.success_message).to_be_visible()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(notes_workflow.email, notes_workflow.password)

    notes_page = NotesPage(page)
    expect(page).to_have_url(re.compile(r"/notes/app/?$"))
    expect(notes_page.my_notes).to_be_visible()
    expect(notes_page.add_note_button).to_be_visible()


@pytest.mark.order(2)
def test_02_create_note_and_check_its_text(notes_workflow):
    notes_page = NotesPage(notes_workflow.page)
    notes_page.create_note(notes_workflow.title, notes_workflow.original_text)

    expect(notes_page.note_card(notes_workflow.title)).to_be_visible()
    expect(notes_page.note_description(notes_workflow.title)).to_contain_text(
        notes_workflow.original_text
    )


@pytest.mark.order(3)
def test_03_edit_then_delete_note(notes_workflow):
    notes_page = NotesPage(notes_workflow.page)
    expect(notes_page.note_card(notes_workflow.title)).to_be_visible()

    notes_page.edit_note(notes_workflow.title, notes_workflow.updated_text)
    expect(notes_page.note_description(notes_workflow.title)).to_contain_text(
        notes_workflow.updated_text
    )
    expect(notes_page.note_description(notes_workflow.title)).not_to_contain_text(
        notes_workflow.original_text
    )

    notes_page.delete_note(notes_workflow.title)
    expect(notes_page.note_card(notes_workflow.title)).to_have_count(0)
