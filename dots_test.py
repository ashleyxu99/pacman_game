from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    ds1 = Dots(600, 600, 150, 450, 150, 450)
    ds2 = Dots(600, 600, 150, 450, 150, 450)
    ds1.eat(150, 150)
    ds2.eat(0, 150)
    assert ds1.top_row[2].x != 150 and ds1.left_col[2].y != 150
    assert ds2.top_row[0].x != 0 and ds2.top_row[-1].x != 600


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
