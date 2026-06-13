---
entity_id: "molecule.ecocyc.Beta-Lactams"
entity_type: "small_molecule"
name: "a β-lactam"
source_database: "EcoCyc"
source_id: "Beta-Lactams"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a β-lactam

`molecule.ecocyc.Beta-Lactams`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Beta-Lactams`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This compound class stands for Lactams lactams in which the amide bond is contained within a four-membered ring, which includes the amide nitrogen and the carbonyl carbon. β-Lactam compounds imitate the naturally occurring D-ALA-D-ALA substrate for the group of enzymes known as penicillin binding proteins (PBPs), which cross-link the peptidoglycan in bacterial cell wall, and thus act as powerful antibiotics . Naturally occurring Beta-Lactams "β-lactam antibiotics" are classified into several groups according to their chemical structure: In Monolactams monolactams the β-lactam ring is not fused to another ring. This class includes compounds such as the Nocardicins nocardicins and the Monobactams monobactams . In Penams penams the β-lactam ring is fused to a saturated five atom ring (a 4:5 structure). Penams contain a sulfur atom at position 1 of the five atom ring (for example, the PENICILLIN penicillins) . Related classes include the Carbapenams carbapenams, which contain a carbon atom in that position , and the Clavams oxopenams (also known as clavams), which contain an oxygen atom at that position (e.g. CPD-9261) . Penems Penems are molecues similar to penams in which the five atom ring is unsaturated at positions 2-3. Similarly, penems contain a sulfur atom at position 1 of the five atom ring, while Carbapenems carbapenems contains a carbon atom in that position...

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

This compound class stands for Lactams lactams in which the amide bond is contained within a four-membered ring, which includes the amide nitrogen and the carbonyl carbon. β-Lactam compounds imitate the naturally occurring D-ALA-D-ALA substrate for the group of enzymes known as penicillin binding proteins (PBPs), which cross-link the peptidoglycan in bacterial cell wall, and thus act as powerful antibiotics . Naturally occurring Beta-Lactams "β-lactam antibiotics" are classified into several groups according to their chemical structure: In Monolactams monolactams the β-lactam ring is not fused to another ring. This class includes compounds such as the Nocardicins nocardicins and the Monobactams monobactams . In Penams penams the β-lactam ring is fused to a saturated five atom ring (a 4:5 structure). Penams contain a sulfur atom at position 1 of the five atom ring (for example, the PENICILLIN penicillins) . Related classes include the Carbapenams carbapenams, which contain a carbon atom in that position , and the Clavams oxopenams (also known as clavams), which contain an oxygen atom at that position (e.g. CPD-9261) . Penems Penems are molecues similar to penams in which the five atom ring is unsaturated at positions 2-3. Similarly, penems contain a sulfur atom at position 1 of the five atom ring, while Carbapenems carbapenems contains a carbon atom in that position . In Cephams cephams and Cephems cephems the β-lactam ring is fused to a six-atom ring (a 4:6 strcuture) that contains a sulfur atom at position 1. In cephams the ring is saturated, while cephems have an unsaturated bond at positions 3-4 . 1-Oxocephams/1-oxacephems conain an oxygen atom at position 1 .

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-380|reaction.ecocyc.TRANS-RXN-380]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.BETA-LACTAMASE-RXN|reaction.ecocyc.BETA-LACTAMASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-380|reaction.ecocyc.TRANS-RXN-380]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Beta-Lactams`
- `METANETX:MNXM10814`
- `CHEBI:35627`
- `LIGAND-CPD:C01866`
