from ase.io import read, write
from icet import ClusterSpace
from icet.tools.structure_generation import generate_sqs_from_supercells

lattice_const = 6.06
primitive = read('unit.POSCAR')
primitive.set_cell(3*[lattice_const], scale_atoms=True)
supercell = primitive.repeat((3,3,3))
halides = [['Pb'], ['Br', 'I'], ['Br', 'I'], ['Br', 'I']]
molecules = [['C'], ['N'], ['H'], ['H'], ['H'], ['H'], ['H'], ['H']]
cs = ClusterSpace(primitive, [12.0, 6.0], molecules + halides)
target_concentrations = {'Br': 47./81, 'I': 34./81}
sqs = generate_sqs_from_supercells(cs,
                                   supercells=[supercell],
                                   target_concentrations=target_concentrations)

write('big_sqs.xyz', sqs)
write('big_sqs.cif', sqs)
