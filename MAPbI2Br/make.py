from ase.io import read, write
from icet import ClusterSpace
from icet.tools.structure_generation import generate_sqs_from_supercells

primitive = read('unit.POSCAR')
supercell = primitive.repeat((3,3,3))
halides = [['Pb'], ['Br', 'I'], ['Br', 'I'], ['Br', 'I']]
molecules = [['C'], ['N'], ['H'], ['H'], ['H'], ['H'], ['H'], ['H']]
cs = ClusterSpace(primitive, [10.0, 5.0], molecules + halides)
target_concentrations = {'Br': 1./3, 'I': 2./3}
sqs = generate_sqs_from_supercells(cs,
                                   supercells=[supercell],
                                   target_concentrations=target_concentrations)

write('big_sqs.xyz', sqs)
write('big_sqs.cif', sqs)
