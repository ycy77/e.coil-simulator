---
entity_id: "reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "ASPARAGINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ASPARAGINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ASPARAGINYL-TRNA SYNTHETASE"
---

# ASPARAGINE--TRNA-LIGASE-RXN

`reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARAGINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASN-tRNAs + ASN + ATP -> Charged-ASN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASN-tRNAs + ASN + ATP -> Charged-ASN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by asparagine—tRNA ligase (complex.ecocyc.ASNS-CPLX). Substrates: ATP (molecule.C00002), L-Asparagine (molecule.C00152). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

ASN-tRNAs + ASN + ATP -> Charged-ASN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ASNS-CPLX|complex.ecocyc.ASNS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ASPARAGINE--TRNA-LIGASE-RXN`

## Notes

ASN-tRNAs + ASN + ATP -> Charged-ASN-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
