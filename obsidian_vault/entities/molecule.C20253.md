---
entity_id: "molecule.C20253"
entity_type: "small_molecule"
name: "Aminoacrylate"
source_database: "KEGG"
source_id: "C20253"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Aminoacrylate"
  - "(Z)-3-Aminoacrylate"
---

# Aminoacrylate

`molecule.C20253`

## Static

- Type: `small_molecule`
- Source: `KEGG:C20253`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Aminoacrylate; (Z)-3-Aminoacrylate EcoCyc common name: (Z)-3-aminoacrylate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Aminoacrylate; (Z)-3-Aminoacrylate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R12625|reaction.R12625]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_product_of` --> [[reaction.ecocyc.RXN-12894|reaction.ecocyc.RXN-12894]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6460|reaction.ecocyc.RXN0-6460]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6452|reaction.ecocyc.RXN0-6452]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C20253`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
