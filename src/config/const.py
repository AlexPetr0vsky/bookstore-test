class Selector:
    # HTML tags
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"

    # Selectors
    SEARCH_INPUT = "input[name='book']"
    SEARCH_BUTTON = "button[type='submit']"
    BOOK_CARD = ".product"
    BOOK_TITLE_LINK = ".product-title a"
    BOOK_DESC_LINK = ".product-desc a"

    # Navigation
    NAV_MAIN = "a:has-text('Main')"
    NAV_AUTHORS = "a:has-text('Authors')"
    NAV_CONTACTS = "a:has-text('Contacts')"
    NAV_SIGN_IN = "a:has-text('Sign in')"
    NAV_REGISTER = "a:has-text('Register')"

class SearchConst:
    NOTHING_WAS_FOUND = "Nothing was found. Please try again!"
