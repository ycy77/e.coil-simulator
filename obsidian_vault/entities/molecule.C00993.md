---
entity_id: "molecule.C00993"
entity_type: "small_molecule"
name: "D-Alanyl-D-alanine"
source_database: "KEGG"
source_id: "C00993"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Alanyl-D-alanine"
  - "D-Ala-D-Ala"
---

# D-Alanyl-D-alanine

`molecule.C00993`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00993`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Alanyl-D-alanine; D-Ala-D-Ala

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: D-Alanyl-D-alanine; D-Ala-D-Ala

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01150|reaction.R01150]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_product_of` --> [[reaction.ecocyc.DALADALALIG-RXN|reaction.ecocyc.DALADALALIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.4.13.22-RXN|reaction.ecocyc.3.4.13.22-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DALADALALIG-RXN|reaction.ecocyc.DALADALALIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00993`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
