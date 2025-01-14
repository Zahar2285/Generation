def all_variants(text):
    """
    Генератор all_variants принимает строку text и возвращает все возможные
    подпоследовательности строки (включая одиночные символы, пары символов и т. д.).
    """
    n = len(text)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = text[start:start + length]
            yield substring
a = all_variants("abc")
for i in a:
   print(i)
