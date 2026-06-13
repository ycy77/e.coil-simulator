---
entity_id: "reaction.ecocyc.RXN-22554"
entity_type: "reaction"
name: "RXN-22554"
source_database: "EcoCyc"
source_id: "RXN-22554"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22554

`reaction.ecocyc.RXN-22554`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22554`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction represents the transport of lipoprotein precursors from their site of synthesis in the cytoplasm through the cytoplasmic membrane by the SEC-SECRETION-CPLX Sec secretion complex or by the TATABCE-CPLX. EcoCyc reaction equation: Prolipoprotein-Cysteines -> Prolipoprotein-Cysteines; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the transport of lipoprotein precursors from their site of synthesis in the cytoplasm through the cytoplasmic membrane by the SEC-SECRETION-CPLX Sec secretion complex or by the TATABCE-CPLX.

## Biological Role

Substrates: a [prolipoprotein]-L-cysteine (molecule.ecocyc.Prolipoprotein-Cysteines). Products: a [prolipoprotein]-L-cysteine (molecule.ecocyc.Prolipoprotein-Cysteines).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

This reaction represents the transport of lipoprotein precursors from their site of synthesis in the cytoplasm through the cytoplasmic membrane by the SEC-SECRETION-CPLX Sec secretion complex or by the TATABCE-CPLX.

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.Prolipoprotein-Cysteines|molecule.ecocyc.Prolipoprotein-Cysteines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Prolipoprotein-Cysteines|molecule.ecocyc.Prolipoprotein-Cysteines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22554`

## Notes

Prolipoprotein-Cysteines -> Prolipoprotein-Cysteines; direction=PHYSIOL-LEFT-TO-RIGHT
