from invocations import checks, docs, travis
from invocations.packaging import release
from invoke import Collection

ns = Collection(release, docs, travis, checks.blacken)
ns.configure(
    {
        "packaging": {
            "sign": True,
            "wheel": True,
            "changelog_file": "docs/changelog.rst",
        }
    }
)
