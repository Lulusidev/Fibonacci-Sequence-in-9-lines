#!/usr/bin/env python3
from functools import lru_cache
@lru_cache
def fibonacci(number: int) -> int:
	return 1 if number <= 1 else (fibonacci(number - 1) + fibonacci(number - 2))
print(fibonacci(int(input('Tamanho da fibonacci sequence que você quer: '))))
