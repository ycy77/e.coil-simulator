---
entity_id: "reaction.ecocyc.RXN-23933"
entity_type: "reaction"
name: "RXN-23933"
source_database: "EcoCyc"
source_id: "RXN-23933"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23933

`reaction.ecocyc.RXN-23933`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23933`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRP-tRNAs + D-TRYPTOPHAN + ATP -> D-Tryptophanyl-tRNA-Trp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TRP-tRNAs + D-TRYPTOPHAN + ATP -> D-Tryptophanyl-tRNA-Trp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tryptophan—tRNA ligase (complex.ecocyc.TRPS-CPLX). Substrates: ATP (molecule.C00002), D-tryptophan (molecule.ecocyc.D-TRYPTOPHAN). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

TRP-tRNAs + D-TRYPTOPHAN + ATP -> D-Tryptophanyl-tRNA-Trp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TRPS-CPLX|complex.ecocyc.TRPS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-TRYPTOPHAN|molecule.ecocyc.D-TRYPTOPHAN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23933`

## Notes

TRP-tRNAs + D-TRYPTOPHAN + ATP -> D-Tryptophanyl-tRNA-Trp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
