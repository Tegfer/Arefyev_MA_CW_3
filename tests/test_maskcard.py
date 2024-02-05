from src.func import mask_card


def test_maskcard():
    card_dt = "MasterCard 7158300734726758"
    masked_card = mask_card(card_dt)
    assert masked_card == '7158 30** **** 6758'
