class Molecule(object):
    '''A molecule with a name and a list of Atoms.'''

    def __init__(self, name):
        '''Create a Compound named name with no Atoms.'''

        self.name = name
        self.atoms = []

    def add(self, a):
        '''Add Atom a to my list of Atoms.'''

        self.atoms.append(a)

    def __repr__(self):
        '''Return a string representation of this molecule in this format:

          Molecule("NAME", (ATOM1, ATOM2, ...))
        '''

        res = ''
        for atom in self.atoms:
            res = res + repr(atom) + ', '

        # Strip off the last comma.
        res = res[:-2]
        return 'Molecule("%s", (%s))' % (self.name, res)

    def __str__(self):
        '''Return a string representation of this Molecule in this format:

          (NAME, (ATOM1, ATOM2, ...))
        '''

        res = ''
        for atom in self.atoms:
            res = res + str(atom) + ', '

        # Strip off the last comma.
        res = res[:-2]
        return '(%s, (%s))' % (self.name, res)

    def translate(self, x, y, z):
        '''Move this Compound, including all atoms, by (x, y, z).'''

        for atom in self.atoms:
            atom.translate(x, y, z)
