from pathlib import Path

PATH_CONFIG = Path(__file__).parent
PATH_SRC = PATH_CONFIG.parent
PATH_PROJECT_ROOT = PATH_SRC.parent
PATH_DATA = PATH_PROJECT_ROOT / "data"
PATH_EXPERIMENTS = PATH_PROJECT_ROOT / "experiments"
PATH_DATA_RAW = PATH_PROJECT_ROOT / "data" / "raw"
PATH_DATA_INTERIM = PATH_PROJECT_ROOT / "data" / "interim"
PATH_DATA_PROCESSED = PATH_PROJECT_ROOT / "data" / "processed"
PATH_SAVED_MODELS = PATH_PROJECT_ROOT / "models"
PATH_NOTEBOOKS = PATH_PROJECT_ROOT / "notebooks"
PATH_REPORTS = PATH_PROJECT_ROOT / "reports"
PATH_TESTS = PATH_PROJECT_ROOT / "tests"

"""
if data is stored outside the project, point an environment variable "DATASETS" to the dir 
and uncomment the line below
"""


# PATH_DATA = Path(os.environ["DATASETS"])

def test_path_definitions():
    """
    tests that the path definitions are correct
    """
    assert str(PATH_CONFIG).endswith("src\\config"), \
        "config path not correct, check src/config/definitions.py"
    assert str(PATH_SRC).endswith(str(PATH_PROJECT_ROOT / "src")), \
        "src path not correct, check src/config/definitions.py"
    assert str(PATH_DATA).endswith(str(PATH_PROJECT_ROOT / "data")), \
        "data path not correct, check src/config/definitions.py"
    assert str(PATH_EXPERIMENTS).endswith(str(PATH_PROJECT_ROOT / "experiments")), \
        "experiments path not correct, check src/config/definitions.py"
    assert str(PATH_DATA_RAW).endswith("data\\raw"), \
        "raw data path not correct, check src/config/definitions.py"
    assert str(PATH_DATA_INTERIM).endswith(
        "data\\interim"), "interim data path not correct, check src/config/definitions.py"
    assert str(PATH_DATA_PROCESSED).endswith(
        "data\\processed"), "processed data path not correct, check src/config/definitions.py"
    assert str(PATH_SAVED_MODELS).endswith(str(PATH_PROJECT_ROOT / "models")), \
        "saved models path not correct, check src/config/definitions.py"
    assert str(PATH_NOTEBOOKS).endswith(str(PATH_PROJECT_ROOT / "notebooks")), \
        "notebooks path not correct, check src/config/definitions.py"
    assert str(PATH_REPORTS).endswith(str(PATH_PROJECT_ROOT / "reports")), \
        "reports path not correct, check src/config/definitions.py"
    assert str(PATH_TESTS).endswith(str(PATH_PROJECT_ROOT / "tests")), \
        "tests path not correct, check src/config/definitions.py"

    print("\nConfigured paths:\n")
    print(PATH_CONFIG)
    print(PATH_SRC)
    print(PATH_PROJECT_ROOT)
    print(PATH_DATA)
    print(PATH_DATA_RAW)
    print(PATH_DATA_INTERIM)
    print(PATH_DATA_PROCESSED)
    print(PATH_SAVED_MODELS)
    print(PATH_NOTEBOOKS)
    print(PATH_REPORTS)
    print(PATH_TESTS)
    print("\nPaths configured correctly!")


if __name__ == "__main__":
    test_path_definitions()
