def test_post(api):

    post = api.get_post(1)

    assert post["id"] == 1
    assert post["userId"] == 1