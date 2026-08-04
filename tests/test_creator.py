from creator_os import CreatorProfile


def test_creator_profile_introduction() -> None:
    profile = CreatorProfile(name="Nova", niche="responsible AI")

    assert profile.introduction() == "Nova creates content about responsible AI."
