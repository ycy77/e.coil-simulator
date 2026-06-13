---
entity_id: "molecule.C01762"
entity_type: "small_molecule"
name: "Xanthosine"
source_database: "KEGG"
source_id: "C01762"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Xanthosine"
---

# Xanthosine

`molecule.C01762`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01762`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Xanthosine

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Xanthosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7681|complex.ecocyc.CPLX0-7681]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-31|reaction.ecocyc.TRANS-RXN-31]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-363|reaction.ecocyc.RXN0-363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5358|reaction.ecocyc.RXN0-5358]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-31|reaction.ecocyc.TRANS-RXN-31]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN|reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P45562|protein.P45562]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01762`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
