---
entity_id: "molecule.C01112"
entity_type: "small_molecule"
name: "D-Arabinose 5-phosphate"
source_database: "KEGG"
source_id: "C01112"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Arabinose 5-phosphate"
---

# D-Arabinose 5-phosphate

`molecule.C01112`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01112`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Arabinose 5-phosphate EcoCyc common name: aldehydo-D-arabinose 5-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: D-Arabinose 5-phosphate

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (7)

- `is_substrate_of` --> [[reaction.R01530|reaction.R01530]] `KEGG` `database` - C01112 <=> C00199
- `is_substrate_of` --> [[reaction.ecocyc.DARAB5PISOM-RXN|reaction.ecocyc.DARAB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16804|reaction.ecocyc.RXN-16804]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RIB5PISOM-RXN|reaction.ecocyc.RIB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-313|reaction.ecocyc.RXN0-313]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01112`
- `EcoCyc:Arabinose-5P`
- `canonicalized_from:molecule.ecocyc.Arabinose-5P`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.Arabinose-5P: EcoCyc:Arabinose-5P
