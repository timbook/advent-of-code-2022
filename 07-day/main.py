from pathlib import Path
import pdb

cmds = open('input.txt', 'r').read().strip().split('\n$ ')[1:]

path_map = {}

cwd = Path('/')

class LsResult:
    def __init__(self, cwd, files):
        self.dirs = []
        self.file_size = 0
        for f in files:
            if f[0] == 'd':
                self.dirs.append((cwd / f[2]).as_posix())
            elif f[0] == 'f':
                self.file_size += f[1]

    def size(self):
        return self.file_size + sum([path_map[d].size() for d in self.dirs])
                
for cmd in cmds:
    if cmd[:2] == 'cd':
        _, dest = cmd.split()
        cwd = (cwd / dest).resolve()
    elif cmd[:2] == 'ls':
        ls = cmd[3:].split('\n')
        files = []
        for res in ls:
            if res[:3] == 'dir':
                _, name = res.split()                
                files.append(('d', 0, name))
            else:
                size, name = res.split()
                files.append(('f', int(size), name))

        path_map[cwd.as_posix()] = LsResult(cwd, files)

sol_a = 0
for dirname, ls_res in path_map.items():
    ls_size = ls_res.size()
    if ls_size <= 100_000:
        sol_a += ls_size

print(f"A ::: {sol_a}")

total_used = path_map['/'].size()
free_space = 70_000_000 - total_used
need_to_free = 30_000_000 - free_space

can_delete = []
for dirname, ls_res in path_map.items():
    ls_size = ls_res.size()
    if ls_size >= need_to_free:
        can_delete.append((dirname, ls_size))

f_del, s_del = min(can_delete, key=lambda t: t[1])
print(f"B ::: {s_del} from {f_del}")
