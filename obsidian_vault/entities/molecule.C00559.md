---
entity_id: "molecule.C00559"
entity_type: "small_molecule"
name: "Deoxyadenosine"
source_database: "KEGG"
source_id: "C00559"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxyadenosine"
  - "2'-Deoxyadenosine"
---

# Deoxyadenosine

`molecule.C00559`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00559`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxyadenosine; 2'-Deoxyadenosine EcoCyc common name: 2'-deoxyadenosine.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Deoxyadenosine; 2'-Deoxyadenosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.RXN-14161|reaction.ecocyc.RXN-14161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14524|reaction.ecocyc.RXN-14524]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108C|reaction.ecocyc.TRANS-RXN-108C]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ADDALT-RXN|reaction.ecocyc.ADDALT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DEOXYADENPHOSPHOR-RXN|reaction.ecocyc.DEOXYADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15140|reaction.ecocyc.RXN-15140]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108C|reaction.ecocyc.TRANS-RXN-108C]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00559`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
