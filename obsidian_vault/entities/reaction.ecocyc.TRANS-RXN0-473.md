---
entity_id: "reaction.ecocyc.TRANS-RXN0-473"
entity_type: "reaction"
name: "acetylmaltose export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# acetylmaltose export

`reaction.ecocyc.TRANS-RXN0-473`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-473`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

Acetylmaltose is excreted into the culture medium by malB+malQ strains which can accumulate maltose but not metabolise it . The MALTACETYLTRAN-CPLX "maa" gene encodes maltose acetyltransferase. EcoCyc reaction equation: ACETYLMALTOSE -> ACETYLMALTOSE; direction=PHYSIOL-LEFT-TO-RIGHT. Acetylmaltose is excreted into the culture medium by malB+malQ strains which can accumulate maltose but not metabolise it . The MALTACETYLTRAN-CPLX "maa" gene encodes maltose acetyltransferase.

## Biological Role

Substrates: 1-O-acetyl-α-maltose (molecule.ecocyc.ACETYLMALTOSE). Products: 1-O-acetyl-α-maltose (molecule.ecocyc.ACETYLMALTOSE).

## Annotation

Acetylmaltose is excreted into the culture medium by malB+malQ strains which can accumulate maltose but not metabolise it . The MALTACETYLTRAN-CPLX "maa" gene encodes maltose acetyltransferase.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.ACETYLMALTOSE|molecule.ecocyc.ACETYLMALTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.ACETYLMALTOSE|molecule.ecocyc.ACETYLMALTOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-473`

## Notes

ACETYLMALTOSE -> ACETYLMALTOSE; direction=PHYSIOL-LEFT-TO-RIGHT
