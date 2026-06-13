---
entity_id: "molecule.C12621"
entity_type: "small_molecule"
name: "trans-3-Hydroxycinnamate"
source_database: "KEGG"
source_id: "C12621"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-3-Hydroxycinnamate"
  - "(2E)-3-(3-Hydroxyphenyl)prop-2-enoate"
---

# trans-3-Hydroxycinnamate

`molecule.C12621`

## Static

- Type: `small_molecule`
- Source: `KEGG:C12621`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-3-Hydroxycinnamate; (2E)-3-(3-Hydroxyphenyl)prop-2-enoate EcoCyc common name: 3-coumarate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: trans-3-Hydroxycinnamate; (2E)-3-(3-Hydroxyphenyl)prop-2-enoate

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-457|reaction.ecocyc.TRANS-RXN0-457]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10040|reaction.ecocyc.RXN-10040]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-457|reaction.ecocyc.TRANS-RXN0-457]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P77589|protein.P77589]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C12621`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
