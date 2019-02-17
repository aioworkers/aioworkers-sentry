async def test_client(context, post, wait_for_call):
    try:
        1 / 0
    except ZeroDivisionError:
        context.sentry.client.captureException()

    await wait_for_call(post)
