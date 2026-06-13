---
entity_id: "reaction.ecocyc.RXN0-5234"
entity_type: "reaction"
name: "RXN0-5234"
source_database: "EcoCyc"
source_id: "RXN0-5234"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5234

`reaction.ecocyc.RXN0-5234`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5234`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALLO-THR -> ACETALD + GLY; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ALLO-THR -> ACETALD + GLY; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX). Substrates: DL-allothreonine (molecule.ecocyc.ALLO-THR). Products: Glycine (molecule.C00037), Acetaldehyde (molecule.C00084).

## Annotation

ALLO-THR -> ACETALD + GLY; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.ALLO-THR|molecule.ecocyc.ALLO-THR]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5234`

## Notes

ALLO-THR -> ACETALD + GLY; direction=PHYSIOL-LEFT-TO-RIGHT
