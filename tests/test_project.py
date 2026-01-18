import os
import subprocess
import shutil

TEST_DIR = os.path.abspath(os.path.dirname(__file__))


def test_wheel():
    path = os.path.join(TEST_DIR, "test_project")
    result = subprocess.run(
        ["pip", "wheel", "--no-build-isolation", "--verbose", "."],
        capture_output=True,
        text=True,
        cwd=path,
    )
    # Clean up build artifacts
    build_dir = os.path.join(path, "dist")
    egg_dir = os.path.join(path, "test.egg-info")
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    if os.path.exists(egg_dir):
        shutil.rmtree(egg_dir)
    # Assertions
    assert result.returncode == 0, f"Build failed: {result.stderr}"
    assert "Building wheel" in result.stdout


if __name__ == "__main__":
    test_wheel()
