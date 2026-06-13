---
entity_id: "molecule.C03539"
entity_type: "small_molecule"
name: "S-Ribosyl-L-homocysteine"
source_database: "KEGG"
source_id: "C03539"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Ribosyl-L-homocysteine"
  - "S-D-Ribosyl-L-homocysteine"
  - "Ribose-5-S-homocysteine"
  - "S-Ribosylhomocysteine"
  - "S-(5-Deoxy-D-ribos-5-yl)-L-homocysteine"
---

# S-Ribosyl-L-homocysteine

`molecule.C03539`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03539`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Ribosyl-L-homocysteine; S-D-Ribosyl-L-homocysteine; Ribose-5-S-homocysteine; S-Ribosylhomocysteine; S-(5-Deoxy-D-ribos-5-yl)-L-homocysteine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: S-Ribosyl-L-homocysteine; S-D-Ribosyl-L-homocysteine; Ribose-5-S-homocysteine; S-Ribosylhomocysteine; S-(5-Deoxy-D-ribos-5-yl)-L-homocysteine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00194|reaction.R00194]] `KEGG` `database` - C00021 + C00001 <=> C03539 + C00147
- `is_product_of` --> [[reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN|reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN|reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03539`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
