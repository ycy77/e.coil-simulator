---
entity_id: "molecule.C00541"
entity_type: "small_molecule"
name: "Cob(II)alamin"
source_database: "KEGG"
source_id: "C00541"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cob(II)alamin"
  - "Vitamin B12r"
---

# Cob(II)alamin

`molecule.C00541`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00541`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cob(II)alamin; Vitamin B12r Cobalamin is the term used for Cobamides where the cobalt ion is attached to a DIMETHYLBENZIMIDAZOLE lower axial ligand, without specifying the upper axial ligand. It includes several compounds often referred to as vitamin B12, that differ in the upper axial ligand. The functional forms of the B12 vitamin, CPD-9037 and ADENOSYLCOBALAMIN, include either a methyl group or an 5'-deoxyadenosyl group as their upper axial ligand, respectively. Other forms of cobalamin include CPD0-1256 (or its conjugated acid AQUACOBIIIALAMIN) and CPD-315. CPD0-1256 Hydroxocobalamin is a naturally produced form synthesized by many bacterial species, while CPD-315 is a common semi-synthetic form produced from bacterially-synthesized CPD0-1256. Vitamin B12 pills often contain CPD-315, which is converted to the active forms in the body. The cobalt ion embedded in cobalamin may exist in different charges (+1, +2 or +3), and the different forms of the compound are referred to as COB-I-ALAMIN, CPD-1829 and CPD-17105, respectively.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: Cob(II)alamin; Vitamin B12r

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-19341|reaction.ecocyc.RXN-19341]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R12183|reaction.R12183]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19340|reaction.ecocyc.RXN-19340]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00541`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
