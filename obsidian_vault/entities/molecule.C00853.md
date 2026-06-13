---
entity_id: "molecule.C00853"
entity_type: "small_molecule"
name: "Cob(I)alamin"
source_database: "KEGG"
source_id: "C00853"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cob(I)alamin"
  - "Cbl"
  - "Vitamin B12s"
---

# Cob(I)alamin

`molecule.C00853`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00853`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cob(I)alamin; Cbl; Vitamin B12s Cobalamin is the term used for Cobamides attached to a DIMETHYLBENZIMIDAZOLE lower axial ligand of the cobalt ion, without specifying the upper axial ligand. It includes several compounds often referred to as vitamin B12, that differ in the upper axial ligand. The functional forms of the B12 vitamin, CPD-9037 and ADENOSYLCOBALAMIN, include either a methyl group or an 5'-deoxyadenosyl group as their upper axial ligand, respectively. Other forms of cobalamin include CPD0-1256 (or its conjugated acid AQUACOBIIIALAMIN) and CPD-315. CPD0-1256 Hydroxocobalamin is a naturally-produced form synthesized by many bacterial species, while CPD-315 is a common semi-synthetic form produced from bacterially-synthesized CPD0-1256. Vitamin B12 pills often contain CPD-315, which is converted to the active forms in the body. The cobalt ion embedded in cobalamin may exist in different charges (+1, +2 or +3), and the different forms of the compound are referred to as COB-I-ALAMIN, CPD-1829 and CPD-17105, respectively.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Cob(I)alamin; Cbl; Vitamin B12s

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.ABC-5-RXN|reaction.ecocyc.ABC-5-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1565|reaction.ecocyc.RXN0-1565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-5-RXN|reaction.ecocyc.ABC-5-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19341|reaction.ecocyc.RXN-19341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1565|reaction.ecocyc.RXN0-1565]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-5-CPLX|complex.ecocyc.ABC-5-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00853`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
