---
entity_id: "molecule.C05512"
entity_type: "small_molecule"
name: "Deoxyinosine"
source_database: "KEGG"
source_id: "C05512"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxyinosine"
  - "2'-Deoxyinosine"
---

# Deoxyinosine

`molecule.C05512`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05512`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxyinosine; 2'-Deoxyinosine EcoCyc common name: 2'-deoxyinosine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Deoxyinosine; 2'-Deoxyinosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.ADDALT-RXN|reaction.ecocyc.ADDALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108E|reaction.ecocyc.TRANS-RXN-108E]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DEOXYINOPHOSPHOR-RXN|reaction.ecocyc.DEOXYINOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108E|reaction.ecocyc.TRANS-RXN-108E]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05512`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
