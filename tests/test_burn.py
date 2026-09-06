from j2scrub.burn.engine import preview

def test_burn_preview_is_destructive_marked():
    report = preview()
    assert report.actions
    assert all(action.destructive for action in report.actions)
