---
entity_id: "molecule.C01817"
entity_type: "small_molecule"
name: "L-Homocystine"
source_database: "KEGG"
source_id: "C01817"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Homocystine"
  - "Homocystine"
---

# L-Homocystine

`molecule.C01817`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01817`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Homocystine; Homocystine EcoCyc common name: L,L-homocystine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: L-Homocystine; Homocystine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-286|reaction.ecocyc.TRANS-RXN-286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-617|reaction.ecocyc.TRANS-RXN0-617]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-286|reaction.ecocyc.TRANS-RXN-286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-617|reaction.ecocyc.TRANS-RXN0-617]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01817`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
