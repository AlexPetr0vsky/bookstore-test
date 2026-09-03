from pytest_check import check

from src.utils.factory import UserFactory


class TestRegisterUser:
    def test_register_user_1(self, api_client):
        user = UserFactory.create_payload()

        response = api_client.register_user(user)

        check.equal(response.status_code, 201)
        check.is_not_none(response.data.id)
        check.equal(response.data.username, user.username)
        check.equal(response.data.email, user.email)
