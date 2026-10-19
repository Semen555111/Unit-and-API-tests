from playwright.sync_api import Locator, Page


class NotesPage:
    """Page Object интерфейса заметок.

    Локаторы используют роли и ``data-testid``; они совместимы с Playwright Codegen
    и проверены на живой странице.
    """

    def __init__(self, page: Page):
        self.page = page
        self.my_notes: Locator = page.get_by_text("MyNotes", exact=True)
        self.add_note_button: Locator = page.get_by_role(
            "button", name="+ Add Note", exact=True
        )
        self.title_input: Locator = page.locator("#title")
        self.description_input: Locator = page.locator("#description")

    def note_card(self, title: str) -> Locator:
        return self.page.locator(".card").filter(
            has=self.page.get_by_test_id("note-card-title").get_by_text(
                title, exact=True
            )
        )

    def note_description(self, title: str) -> Locator:
        return self.note_card(title).get_by_test_id("note-card-description")

    def create_note(self, title: str, description: str) -> None:
        self.add_note_button.click()
        self.title_input.fill(title)
        self.description_input.fill(description)
        self.page.get_by_role("button", name="Create", exact=True).click()

    def edit_note(self, title: str, new_description: str) -> None:
        self.note_card(title).get_by_test_id("note-edit").click()
        self.description_input.fill(new_description)
        self.page.get_by_role("button", name="Save", exact=True).click()

    def delete_note(self, title: str) -> None:
        self.note_card(title).get_by_test_id("note-delete").click()
        # На странице две кнопки Delete: на карточке и в открытом окне подтверждения.
        self.page.get_by_role("button", name="Delete", exact=True).last.click()
