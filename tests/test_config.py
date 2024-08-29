import os

from src.config import get_config

TEST_DIR = os.path.dirname(__file__)
DB_URL = 'postgresql+asyncpg://test-user:test-password@test-host/test-database'


class TestConfig:
    config = get_config(TEST_DIR + '/' + 'test_config.yml')

    def test_db_values(self):
        assert self.config.database_config.database == 'test-database'

    def test_jwt_values(self):
        assert self.config.jwt_config.private_key == 'test-private-key'

    def test_db_url(self):
        assert self.config.database_config.database_url == DB_URL
