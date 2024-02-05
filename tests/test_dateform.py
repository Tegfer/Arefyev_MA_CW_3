from src.func import date_form


def test_dateform():
    date = "2018-06-30T02:08:58.425572"
    formed_date = date_form(date)
    assert  formed_date == "30.06.2018"
