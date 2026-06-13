---
entity_id: "molecule.C00802"
entity_type: "small_molecule"
name: "Oxalureate"
source_database: "KEGG"
source_id: "C00802"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxalureate"
  - "Oxaluric acid"
  - "Monooxalylurea"
  - "Oxalurate"
  - "N-Carbamoyl-2-oxoglycine"
---

# Oxalureate

`molecule.C00802`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00802`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxalureate; Oxaluric acid; Monooxalylurea; Oxalurate; N-Carbamoyl-2-oxoglycine EcoCyc common name: N-carbamoyl-2-oxoglycine.

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Oxalureate; Oxaluric acid; Monooxalylurea; Oxalurate; N-Carbamoyl-2-oxoglycine

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN|reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.R165-RXN|reaction.ecocyc.R165-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7024|reaction.ecocyc.RXN0-7024]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00802`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
