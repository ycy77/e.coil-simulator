---
entity_id: "molecule.C00054"
entity_type: "small_molecule"
name: "Adenosine 3',5'-bisphosphate"
source_database: "KEGG"
source_id: "C00054"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Adenosine 3',5'-bisphosphate"
  - "PAP"
  - "3'-Phosphoadenylate"
  - "Phosphoadenosine phosphate"
---

# Adenosine 3',5'-bisphosphate

`molecule.C00054`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00054`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Adenosine 3',5'-bisphosphate; PAP; 3'-Phosphoadenylate; Phosphoadenosine phosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Adenosine 3',5'-bisphosphate; PAP; 3'-Phosphoadenylate; Phosphoadenosine phosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.ENTDB-RXN|reaction.ecocyc.ENTDB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOLO-ACP-SYNTH-RXN|reaction.ecocyc.HOLO-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15889|reaction.ecocyc.RXN-15889]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00188|reaction.R00188]] `KEGG` `database` - C00054 + C00001 <=> C00020 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.1.8.4.8-RXN|reaction.ecocyc.1.8.4.8-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN|reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.8.4.8-RXN|reaction.ecocyc.1.8.4.8-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.3.1.13.3-RXN|reaction.ecocyc.3.1.13.3-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00054`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
