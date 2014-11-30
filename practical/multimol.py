from molecule import Molecule
from atom import Atom

import sys

def read_molecule(r):
    '''Read a single molecule from reader r and return it,
    or return None to signal end of file.'''

    # If there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND   name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num kind x y z"
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(num, kind, float(x), float(y), float(z)))

    return molecule

def read_all_molecules(r):
    '''Read zero or more molecules from reader r,
    returning a list of the molecules read.'''

    result = []
    reading = True
    while reading:
        molecule = read_molecule(r)
        if molecule:
            result.append(molecule)
        else:
            reading = False

    return result

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    molecules = read_all_molecules(input_file)
    for m in molecules:
        print m
