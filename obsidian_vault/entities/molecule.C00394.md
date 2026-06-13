---
entity_id: "molecule.C00394"
entity_type: "small_molecule"
name: "GDP-glucose"
source_database: "KEGG"
source_id: "C00394"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GDP-glucose"
  - "GDP-D-glucose"
  - "GDP-alpha-D-glucose"
---

# GDP-glucose

`molecule.C00394`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00394`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GDP-glucose; GDP-D-glucose; GDP-alpha-D-glucose EcoCyc common name: GDP-α-D-glucose.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: GDP-glucose; GDP-D-glucose; GDP-alpha-D-glucose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.GDP-GLUCOSIDASE-RXN|reaction.ecocyc.GDP-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDPSUGARHYDRO-RXN|reaction.ecocyc.UDPSUGARHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00394`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
