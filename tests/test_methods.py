async def test_set_user(context, catch_sentry):
    context.sentry.set_user({"username": "user"})


async def test_set_tag(context, catch_sentry):
    context.sentry.set_tag("a", "1")
