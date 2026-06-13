---
entity_id: "molecule.C05629"
entity_type: "small_molecule"
name: "Phenylpropanoate"
source_database: "KEGG"
source_id: "C05629"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenylpropanoate"
  - "3-Phenylpropanoate"
  - "3-Phenyl-propionic acid"
  - "3-Phenylpropanoic acid"
  - "3-Phenylpropionic acid"
---

# Phenylpropanoate

`molecule.C05629`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05629`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenylpropanoate; 3-Phenylpropanoate; 3-Phenyl-propionic acid; 3-Phenylpropanoic acid; 3-Phenylpropionic acid EcoCyc common name: 3-phenylpropanoate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: Phenylpropanoate; 3-Phenylpropanoate; 3-Phenyl-propionic acid; 3-Phenylpropanoic acid; 3-Phenylpropionic acid

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2081|complex.ecocyc.MONOMER0-2081]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-282|reaction.ecocyc.TRANS-RXN0-282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.HCAMULTI-RXN|reaction.ecocyc.HCAMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4101|reaction.ecocyc.RXN0-4101]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-282|reaction.ecocyc.TRANS-RXN0-282]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN|reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05629`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
