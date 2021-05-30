import z3
from whitesymex import parser
from whitesymex.path_group import PathGroup
from whitesymex.state import State

instructions = parser.parse_file("../release/spaceship.ws")
symflag = [z3.BitVec(f"flag_{i}", 24) for i in range(12)]
stdin = list(b"xctf{") + symflag + list(b"}\n")
state = State.create_entry_state(instructions, stdin=stdin)

# The flag is printable.
for c in symflag:
    state.solver.add(z3.And(0x20 <= c, c <= 0x7F))

path_group = PathGroup(state)
path_group.explore(find=b"crewmember", avoid=b"Imposter!")
flag = path_group.found[0].concretize()
print(flag.decode())
