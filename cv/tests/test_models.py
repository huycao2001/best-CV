from utils.setup_test import TestSetup
from authentication.models import User
from cv.models import CV


class TestModel(TestSetup):

    def test_should_create_user(self):
        user = self.create_test_user()
        cv = CV(owner=user, title="Buy milk", description='get it done')
        cv.save()
        self.assertEqual(str(cv), 'Buy milk')
