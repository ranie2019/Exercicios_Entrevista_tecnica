def phoneword(phonenuber):
    """toda possibilidade do phonewords respequitivo ao phonenuber

    :param phonenuber: str
    :return: lista de str com todo phonewords
    """
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    n = len(phonenuber)

    def phoneword_rec(previus_results, cursor):
        if cursor == n:
            return previus_results
        digit = phonenuber[cursor]
        results = []
        for char in digit_to_chars[digit]:
            results.extend(
                prev_result + char for prev_result in previus_results)
        return phoneword_rec(results, cursor + 1)
    return phoneword_rec([''], 0)

print(phoneword(''))
print(phoneword('7'))
print(phoneword('73'))
print(phoneword('736'))
