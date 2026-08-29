# Releasing aspose-3d-foss to PyPI

This document describes how to publish a release of `aspose-3d-foss` to
[pypi.org](https://pypi.org/project/aspose-3d-foss/).

## One-time setup (project owner)

Publishing uses [Trusted Publishing (PEP 740)](https://docs.pypi.org/trusted-publishers/)
— no PyPI API tokens are stored in GitHub secrets.

1. **Claim the PyPI project** (if it doesn't exist yet): publish the first
   release manually once, or pre-register it at
   <https://pypi.org/manage/account/publishing/>.
2. On PyPI → *Account settings* → *Publishing* → *Add a new pending publisher*:
   - PyPI project name: `aspose-3d-foss`
   - Owner: `aspose-3d` (the GitHub org/user that hosts this repo)
   - Repository: `Aspose.3D-for-Python`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`
3. In the GitHub repo → *Settings* → *Environments* → create an environment
   named `pypi` (optionally restrict it to the `master`/`main` branch).

## Cutting a release

1. Bump `version` in `setup.py` (project uses `MAJOR.MINOR.PATCH`, e.g.
   `26.2.0`; the calendar-year major matches the Aspose.3D release train).
2. Commit and push to `master`.
3. Create a tag and a GitHub Release — either via the web UI, or:
   ```bash
   git tag v26.2.0
   git push origin v26.2.0
   # then create a GitHub Release for the tag (Release → Draft new release)
   ```
   The tag must be the version prefixed with `v` (e.g. `v26.2.0`).
4. Publishing the GitHub Release triggers `.github/workflows/publish.yml`,
   which builds the sdist + wheel, runs `twine check`, verifies the wheel
   version matches the tag, and uploads to PyPI.
5. Verify the package at
   <https://pypi.org/project/aspose-3d-foss/> and with
   `pip install aspose-3d-foss`.

If the version-check step fails (tag doesn't match `setup.py`), fix
`setup.py`, push, delete and re-create the GitHub Release.

## Notes

- The workflow also supports `workflow_dispatch` for build-only dry runs
  from the Actions tab (it builds and checks but does not upload).
- Version check: publishing to PyPI is immutable — a given version string
  can only ever be uploaded once. Never re-publish the same version.
- `python -m build` locally reproduces exactly what CI builds if you want
  to inspect artifacts first (`dist/*.whl`, `dist/*.tar.gz`).
- Every format subpackage under `aspose/threed/formats/` must contain an
  `__init__.py`; without it, `find_packages()` silently drops the directory
  from the wheel while `formats/__init__.py` still imports it — the wheel
  installs but is broken on import.
