def test_connection(bot):
    while (True):
        try:
            question = 'hello'
            print("test connection")
            response = bot.ask(question)
            print(response)
            break
        except Exception as e:
            bot.refresh()
    return response
