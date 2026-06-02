from ase.io import read, write
from icet import ClusterSpace
from icet.tools.structure_generation import generate_sqs_from_supercells

primitive = read('unit.POSCAR')
supercell = primitive.repeat((3,3,3))
halides = [['Pb'], ['Br', 'I'], ['Br', 'I'], ['Br', 'I']]
molecules = [['C'], ['N'], ['H'], ['H'], ['H'], ['H'], ['H'], ['H']]
cs = ClusterSpace(primitive, [10.0, 5.0], molecules + halides)
target_concentrations = {'Br': 2./3, 'I': 1./3}
sqs = generate_sqs_from_supercells(cs,
                                   supercells=[supercell],
                                   target_concentrations=target_concentrations)

write('sqs.xyz', sqs)
write('sqs.cif', sqs)
