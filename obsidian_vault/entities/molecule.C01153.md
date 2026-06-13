---
entity_id: "molecule.C01153"
entity_type: "small_molecule"
name: "Orthophosphoric monoester"
source_database: "KEGG"
source_id: "C01153"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Orthophosphoric monoester"
  - "Phosphate monoester"
---

# Orthophosphoric monoester

`molecule.C01153`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01153`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Orthophosphoric monoester; Phosphate monoester EcoCyc common name: a phosphate monoester. This compound class stands for generic and unspecified phosphate monoester compounds.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Orthophosphoric monoester; Phosphate monoester

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R00626|reaction.R00626]] `KEGG` `database` - C01153 + C00001 <=> C00069 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALKAPHOSPHA-RXN|reaction.ecocyc.ALKAPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01153`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
