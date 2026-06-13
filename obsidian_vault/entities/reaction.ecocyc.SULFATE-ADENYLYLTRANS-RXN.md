---
entity_id: "reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN"
entity_type: "reaction"
name: "SULFATE-ADENYLYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "SULFATE-ADENYLYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SULFATE-ADENYLYLTRANS-RXN

`reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SULFATE-ADENYLYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway. EcoCyc reaction equation: PROTON + SULFATE + ATP -> APS + PPI; direction=LEFT-TO-RIGHT. The first step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway.

## Biological Role

Catalyzed by sulfate adenylyltransferase (complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX). Substrates: ATP (molecule.C00002), Sulfate (molecule.C00059), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), Adenylyl sulfate (molecule.C00224).

## Enriched Pathways

- `ecocyc.PWY-5340` sulfate activation for sulfonation (EcoCyc)

## Annotation

The first step in the activation of sulfate. The reaction occurs early in the sulfide branch of the cysteine synthesis pathway.

## Pathways

- `ecocyc.PWY-5340` sulfate activation for sulfonation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX|complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00224|molecule.C00224]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SULFATE-ADENYLYLTRANS-RXN`

## Notes

PROTON + SULFATE + ATP -> APS + PPI; direction=LEFT-TO-RIGHT
