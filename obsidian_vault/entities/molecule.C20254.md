---
entity_id: "molecule.C20254"
entity_type: "small_molecule"
name: "Ureidoacrylate"
source_database: "KEGG"
source_id: "C20254"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ureidoacrylate"
  - "(Z)-3-Ureidoacrylate"
---

# Ureidoacrylate

`molecule.C20254`

## Static

- Type: `small_molecule`
- Source: `KEGG:C20254`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ureidoacrylate; (Z)-3-Ureidoacrylate EcoCyc common name: (Z)-3-ureidoacrylate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Ureidoacrylate; (Z)-3-Ureidoacrylate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.RXN-20707|reaction.ecocyc.RXN-20707]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6450|reaction.ecocyc.RXN0-6450]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R12625|reaction.R12625]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12894|reaction.ecocyc.RXN-12894]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6460|reaction.ecocyc.RXN0-6460]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C20254`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
