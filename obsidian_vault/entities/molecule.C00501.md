---
entity_id: "molecule.C00501"
entity_type: "small_molecule"
name: "CDP-glucose"
source_database: "KEGG"
source_id: "C00501"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CDP-glucose"
  - "CDP-D-Glucose"
---

# CDP-glucose

`molecule.C00501`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00501`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CDP-glucose; CDP-D-Glucose EcoCyc common name: CDP-α-D-glucose.

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: CDP-glucose; CDP-D-Glucose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.UDPSUGARHYDRO-RXN|reaction.ecocyc.UDPSUGARHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00501`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
