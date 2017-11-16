import pickle


def get_pdb_line(atom='ATOM', atomnum=0, atomname=' ', resname=' ', chain_idx=' ', resnum=0, x=0.0, y=0.0, z=0.0,
                 occ=0.0,
                 bfactor=0.0, element=' '):
    j = [str(atom), str(int(atomnum)), str(atomname), str(resname), str(chain_idx), str(int(resnum)), float(x),
         float(y), float(z), float(occ), float(bfactor), str(element)]
    j[0] = j[0].ljust(6)  # atom#6s
    j[1] = j[1].rjust(5)  # aomnum#5d
    j[2] = j[2].center(4)  # atomname$#4s
    j[3] = j[3].ljust(3)  # resname#1s
    j[4] = j[4].rjust(1)  # Astring
    j[5] = j[5].rjust(4)  # resnum
    j[6] = str('%8.3f' % j[6]).rjust(8)  # x
    j[7] = str('%8.3f' % j[7]).rjust(8)  # y
    j[8] = str('%8.3f' % j[8]).rjust(8)  # z\
    j[9] = str('%6.2f' % (j[9])).rjust(6)  # occ
    j[10] = str('%6.2f' % j[10]).ljust(6)  # temp
    j[11] = j[11].rjust(12)  # elname
    line = ("{}{} {} {} {}{}    {}{}{}{}{}{}".format(
        j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10], j[11]))



    return line


def save_universe(universe, file_path: str) -> bool:
    try:
        with open(file_path, 'wb') as handle:
            pickle.dump(universe, handle)
        return True
    except:
        print('Cannot save to {}'.format(file_path))
        return False


def load_universe(file_path: str):
    try:
        with open(file_path, 'rb') as handle:
            return pickle.load(handle)
    except:
        print('Cannot load from {}'.format(file_path))