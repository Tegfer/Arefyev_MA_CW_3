from src.func import mask_bill


def test_maskbill():
    to = "Счет 35383033474447895560"
    masked_bill = mask_bill(to)
    assert masked_bill == '**5560'
