---
entity_id: "molecule.C00881"
entity_type: "small_molecule"
name: "Deoxycytidine"
source_database: "KEGG"
source_id: "C00881"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxycytidine"
  - "2'-Deoxycytidine"
---

# Deoxycytidine

`molecule.C00881`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00881`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxycytidine; 2'-Deoxycytidine EcoCyc common name: 2'-deoxycytidine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Deoxycytidine; 2'-Deoxycytidine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-14522|reaction.ecocyc.RXN-14522]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5292|reaction.ecocyc.RXN0-5292]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108D|reaction.ecocyc.TRANS-RXN-108D]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CYTIDEAM-RXN|reaction.ecocyc.CYTIDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108D|reaction.ecocyc.TRANS-RXN-108D]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00881`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
