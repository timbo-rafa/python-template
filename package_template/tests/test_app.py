from package_template import increment

class TestApp:
    def test_increment(self):
        arg = 0

        assert increment(0) == 1