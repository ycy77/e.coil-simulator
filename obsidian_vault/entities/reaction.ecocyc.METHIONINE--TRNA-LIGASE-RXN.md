---
entity_id: "reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "METHIONINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "METHIONINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "METHIONYL-TRNA SYNTHETASE"
---

# METHIONINE--TRNA-LIGASE-RXN

`reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHIONINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Elongation-tRNAMet + MET + ATP -> Charged-MET-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Elongation-tRNAMet + MET + ATP -> Charged-MET-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by methionine—tRNA ligase (complex.ecocyc.METG-CPLX). Substrates: ATP (molecule.C00002), L-Methionine (molecule.C00073). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

Elongation-tRNAMet + MET + ATP -> Charged-MET-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.METG-CPLX|complex.ecocyc.METG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:METHIONINE--TRNA-LIGASE-RXN`

## Notes

Elongation-tRNAMet + MET + ATP -> Charged-MET-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
