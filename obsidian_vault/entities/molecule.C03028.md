---
entity_id: "molecule.C03028"
entity_type: "small_molecule"
name: "Thiamin triphosphate"
source_database: "KEGG"
source_id: "C03028"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thiamin triphosphate"
  - "Thiamine triphosphate"
---

# Thiamin triphosphate

`molecule.C03028`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03028`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thiamin triphosphate; Thiamine triphosphate EcoCyc common name: thiamine triphosphate.

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: Thiamin triphosphate; Thiamine triphosphate

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (1)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7041|reaction.ecocyc.RXN0-7041]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C03028`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
