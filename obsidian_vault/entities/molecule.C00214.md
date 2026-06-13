---
entity_id: "molecule.C00214"
entity_type: "small_molecule"
name: "Thymidine"
source_database: "KEGG"
source_id: "C00214"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thymidine"
  - "Deoxythymidine"
---

# Thymidine

`molecule.C00214`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00214`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thymidine; Deoxythymidine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Thymidine; Deoxythymidine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.RXN-14521|reaction.ecocyc.RXN-14521]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN|reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108H|reaction.ecocyc.TRANS-RXN-108H]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108H|reaction.ecocyc.TRANS-RXN-108H]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00214`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
