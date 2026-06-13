---
entity_id: "reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Poly(A) polymerase"
---

# POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN

`reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pcnB (protein.P0ABF1). Substrates: ATP (molecule.C00002), RNA (molecule.C00046). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

ATP + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABF1|protein.P0ABF1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN`

## Notes

ATP + RNA-Holder -> PPI + RNA-Holder; direction=PHYSIOL-LEFT-TO-RIGHT
