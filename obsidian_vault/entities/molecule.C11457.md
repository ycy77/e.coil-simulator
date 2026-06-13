---
entity_id: "molecule.C11457"
entity_type: "small_molecule"
name: "3-(3-Hydroxyphenyl)propanoic acid"
source_database: "KEGG"
source_id: "C11457"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-(3-Hydroxyphenyl)propanoic acid"
  - "Dihydro-3-coumaric acid"
  - "3-Hydroxyphenylpropanoate"
  - "3-(3-Hydroxyphenyl)propanoate"
---

# 3-(3-Hydroxyphenyl)propanoic acid

`molecule.C11457`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11457`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-(3-Hydroxyphenyl)propanoic acid; Dihydro-3-coumaric acid; 3-Hydroxyphenylpropanoate; 3-(3-Hydroxyphenyl)propanoate EcoCyc common name: 3-(3-hydroxyphenyl)propanoate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: 3-(3-Hydroxyphenyl)propanoic acid; Dihydro-3-coumaric acid; 3-Hydroxyphenylpropanoate; 3-(3-Hydroxyphenyl)propanoate

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-1441|complex.ecocyc.MONOMER0-1441]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-61|reaction.ecocyc.TRANS-RXN-61]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MHPHYDROXY-RXN|reaction.ecocyc.MHPHYDROXY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2841|reaction.ecocyc.RXN0-2841]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-61|reaction.ecocyc.TRANS-RXN-61]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P77589|protein.P77589]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C11457`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
