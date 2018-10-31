from tuvok import cli
from helpers.wrap import Wrap


class TestModule(object):
    def setup(self):
        self.main = cli.main

    def teardown(self):
        self.main = None

    def test_warns_if_module_isnt_pinned_git(self, caplog):
        file = 'tests/test_module/module_git_missingref.tf'
        with Wrap(self, [file], expect_exit=True):
            assert ('Modules sourced from GitHub should be pinned FAIL in {}'.format(file)) in caplog.text

    def test_passes_if_module_has_ref_git(self, caplog):
        file = 'tests/test_module/module_git_hasref.tf'
        with Wrap(self, [file], expect_exit=False):
            assert ('Modules sourced from GitHub should be pinned PASS in {}'.format(file)) in caplog.text

    def test_warns_if_module_isnt_pinned_github(self, caplog):
        file = 'tests/test_module/module_github_missingref.tf'
        with Wrap(self, [file], expect_exit=True):
            assert ('Modules sourced from GitHub should be pinned FAIL in {}'.format(file)) in caplog.text

    def test_passes_if_module_has_ref_github(self, caplog):
        file = 'tests/test_module/module_github_hasref.tf'
        with Wrap(self, [file], expect_exit=False):
            assert ('Modules sourced from GitHub should be pinned PASS in {}'.format(file)) in caplog.text

    def test_passes_if_module_not_git(self, caplog):
        file = 'tests/test_module/module_notgit.tf'
        with Wrap(self, [file], expect_exit=False):
            assert ('Modules sourced from GitHub should be pinned FAIL in {}'.format(file)) not in caplog.text
