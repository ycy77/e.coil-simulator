---
entity_id: "molecule.C00151"
entity_type: "small_molecule"
name: "L-Amino acid"
source_database: "KEGG"
source_id: "C00151"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Amino acid"
  - "L-2-Amino acid"
---

# L-Amino acid

`molecule.C00151`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00151`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Amino acid; L-2-Amino acid EcoCyc common name: an L-amino acid.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Amino acid; L-2-Amino acid

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.RXN-23880|reaction.ecocyc.RXN-23880]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23886|reaction.ecocyc.RXN-23886]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00151`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
