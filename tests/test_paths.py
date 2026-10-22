from roadmap_utils.paths import DATA_DIR, PROCESSED_DIR, RAW_DIR, REPO_ROOT


def test_repo_root_contains_pyproject():
    assert (REPO_ROOT / "pyproject.toml").exists()


def test_data_dirs_live_inside_data():
    assert RAW_DIR.parent == DATA_DIR
    assert PROCESSED_DIR.parent == DATA_DIR
