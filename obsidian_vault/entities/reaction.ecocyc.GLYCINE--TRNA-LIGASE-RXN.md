---
entity_id: "reaction.ecocyc.GLYCINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "GLYCINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "GLYCINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLYCYL-TRNA SYNTHETASE"
---

# GLYCINE--TRNA-LIGASE-RXN

`reaction.ecocyc.GLYCINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLY-tRNAs + GLY + ATP -> Charged-GLY-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLY-tRNAs + GLY + ATP -> Charged-GLY-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glycine—tRNA ligase (complex.ecocyc.GLYS-CPLX). Substrates: ATP (molecule.C00002), Glycine (molecule.C00037). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

GLY-tRNAs + GLY + ATP -> Charged-GLY-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.GLYS-CPLX|complex.ecocyc.GLYS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCINE--TRNA-LIGASE-RXN`

## Notes

GLY-tRNAs + GLY + ATP -> Charged-GLY-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
