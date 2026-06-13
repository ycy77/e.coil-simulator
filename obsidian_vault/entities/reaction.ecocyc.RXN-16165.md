---
entity_id: "reaction.ecocyc.RXN-16165"
entity_type: "reaction"
name: "RXN-16165"
source_database: "EcoCyc"
source_id: "RXN-16165"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16165

`reaction.ecocyc.RXN-16165`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16165`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Initiation-tRNAmet + MET + ATP -> L-methionyl-tRNAfmet + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Initiation-tRNAmet + MET + ATP -> L-methionyl-tRNAfmet + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by methionine—tRNA ligase (complex.ecocyc.METG-CPLX). Substrates: ATP (molecule.C00002), L-Methionine (molecule.C00073). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

Initiation-tRNAmet + MET + ATP -> L-methionyl-tRNAfmet + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.METG-CPLX|complex.ecocyc.METG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-16165`

## Notes

Initiation-tRNAmet + MET + ATP -> L-methionyl-tRNAfmet + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
