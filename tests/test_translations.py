def test_get_country_locale_en():
    from py_i18n_countries import get_country

    assert get_country(code="us", locale="en") == "United States of America"
    assert get_country(code="is", locale="en") == "Iceland"


def test_get_nationality_locale_en():
    from py_i18n_countries import get_nationality

    assert get_nationality(code="us", locale="en") == "American"
    assert get_nationality(code="is", locale="en") == "Icelandic"


def test_get_country_case_insensitive():
    from py_i18n_countries import get_country

    assert get_country("us") == get_country("US")
