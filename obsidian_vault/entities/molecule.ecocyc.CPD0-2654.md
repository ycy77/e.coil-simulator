---
entity_id: "molecule.ecocyc.CPD0-2654"
entity_type: "small_molecule"
name: "a pyruvoyl cofactor"
source_database: "EcoCyc"
source_id: "CPD0-2654"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a pyruvoyl group"
---

# a pyruvoyl cofactor

`molecule.ecocyc.CPD0-2654`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CPD0-2654`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Several enzymes depend on a covalently bound CPD0-2654 "pyruvoyl cofactor" for activity . These enzymes catalyze either the reduction or the decarboxylation of amino acids and amino acid derivatives. Pyruvoyl-dependent reductases, such as EC-1.21.4.1, EC-1.21.4.2, EC-1.21.4.3, and EC-1.21.4.4, have been described mostly from Gram-positive anaerobes performing Stickland reactions, although they can be found in Gram-negative bacteria, such as the CPLX-9661 of TAX-876. Decarboxylases, such as EC-4.1.1.11, EC-4.1.1.22, EC-4.1.1.65, and EC-4.1.1.50, have been described in a wide range of bacteria as well as in mammals. The pyruvoyl group is thought to act analogously to a PYRIDOXAL_PHOSPHATE cofactor by first forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the reaction . In many cases, the eukaryotic homologs of these enzymes utilize PYRIDOXAL_PHOSPHATE instead of the pyruvoyl group. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents. Pyruvoyl-containing enzymes are expressed as proenzymes (also known as zymogens or π proteins), which undergo a post-translational self-maturation/cleavage that generates two chains, β and α (by convention β is the N-terminal chain and α is the C-terminal chain)...

## Biological Role

Binds phosphatidylserine decarboxylase (complex.ecocyc.PHOSPHASERDECARB-DIMER), S-adenosylmethionine decarboxylase (complex.ecocyc.SAMDECARB-CPLX).

## Annotation

Several enzymes depend on a covalently bound CPD0-2654 "pyruvoyl cofactor" for activity . These enzymes catalyze either the reduction or the decarboxylation of amino acids and amino acid derivatives. Pyruvoyl-dependent reductases, such as EC-1.21.4.1, EC-1.21.4.2, EC-1.21.4.3, and EC-1.21.4.4, have been described mostly from Gram-positive anaerobes performing Stickland reactions, although they can be found in Gram-negative bacteria, such as the CPLX-9661 of TAX-876. Decarboxylases, such as EC-4.1.1.11, EC-4.1.1.22, EC-4.1.1.65, and EC-4.1.1.50, have been described in a wide range of bacteria as well as in mammals. The pyruvoyl group is thought to act analogously to a PYRIDOXAL_PHOSPHATE cofactor by first forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the reaction . In many cases, the eukaryotic homologs of these enzymes utilize PYRIDOXAL_PHOSPHATE instead of the pyruvoyl group. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents. Pyruvoyl-containing enzymes are expressed as proenzymes (also known as zymogens or π proteins), which undergo a post-translational self-maturation/cleavage that generates two chains, β and α (by convention β is the N-terminal chain and α is the C-terminal chain). An CYS residue was shown to be the precursor of the pyruvoyl group in the reductases, while an SER residue is the precursor in the decarboxylases . While the exact process of pyruvoyl group formation in reductases (from an CYS residue) is still not understood, the process is much better understood in the case of the decarboxylases. The self-cleavage reaction occurs through nonhydrolytic serinolysis, in which the side chain hydroxyl group of the seri

## Outgoing Edges (2)

- `binds` --> [[complex.ecocyc.PHOSPHASERDECARB-DIMER|complex.ecocyc.PHOSPHASERDECARB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.SAMDECARB-CPLX|complex.ecocyc.SAMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:CPD0-2654`
