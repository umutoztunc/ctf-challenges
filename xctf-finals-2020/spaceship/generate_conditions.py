#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import List, Tuple
import random
import sys

from Crypto.Util.number import getPrime


@dataclass
class Equation:
    lhs: List[Tuple[int, int]] = field(default_factory=list)
    rhs: int = 0


def random_coefficient(n=10):
    coeff = random.randint(1, n)
    return coeff


def random_equations(values, indexes, modulus) -> List[Equation]:
    equations = []
    n = len(indexes)
    for _ in range(n):
        coeffs = [random_coefficient() for _ in range(n)]
        eq = Equation()
        for coeff, index in zip(coeffs, indexes):
            eq.lhs.append((coeff, index))
            eq.rhs += coeff * values[index]

        eq.rhs %= modulus
        equations.append(eq)
    return equations


def generate_equations(values, group_size) -> Tuple[List[Equation], int]:
    modulus = getPrime(12)
    indexes = list(range(len(values)))
    random.shuffle(indexes)
    equations = []
    while indexes:
        index_group = [indexes.pop() for _ in range(group_size)]
        eqs = random_equations(values, index_group, modulus)
        equations.extend(eqs)
    random.shuffle(equations)
    return equations, modulus


def create_header_file(flag_length, prime_modulus, equations: List[Equation]):
    assert equations, 'Equations should not be empty.'
    eq_size = len(equations[0].lhs) * 2 + 1

    with open('src/spaceship.h', 'w') as f:
        f.write(f'#define FLAG_LENGTH {flag_length}\n')
        f.write(f'#define PRIME_MODULUS {prime_modulus}\n')
        f.write('\n')
        f.write(f'int equations[][{eq_size}] = {{\n')
        for equation in equations:
            f.write('\t{')
            for coeff, index in equation.lhs:
                f.write(f'{hex(coeff)}, {hex(index)}, ')
            f.write(hex(equation.rhs))
            f.write('},\n')
        f.write('};\n')


def main():
    if len(sys.argv) > 1:
        group_size = int(sys.argv[1])
    else:
        group_size = 3

    with open('flag', 'r') as f:
        flag = f.read().rstrip()

    if len(flag) % group_size:
        print('Length of flag is not divisible by group size.')
        return

    values = [ord(c) for c in flag]
    equations, prime_modulus = generate_equations(values, group_size)
    create_header_file(len(flag), prime_modulus, equations)

    print(f'Prime modulus: {prime_modulus}')
    print()
    print('Equations:')
    for equation in equations:
        temp = []
        for coeff, index in equation.lhs:
            s = f'{coeff} * values[{index}]'
            temp.append(s)
        lhs_string = ' + '.join(temp)
        print(f'{lhs_string} == {equation.rhs}')


if __name__ == '__main__':
    main()
