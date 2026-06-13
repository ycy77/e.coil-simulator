---
entity_id: "reaction.ecocyc.COBALADENOSYLTRANS-RXN"
entity_type: "reaction"
name: "COBALADENOSYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "COBALADENOSYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# COBALADENOSYLTRANS-RXN

`reaction.ecocyc.COBALADENOSYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:COBALADENOSYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes adenosylcobalamin. EcoCyc reaction equation: CPD-20905 + ATP + PROTON -> B12-Corrinoid-Adenosyltranferase + P3I; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes adenosylcobalamin.

## Biological Role

Catalyzed by btuR (protein.P0A9H5). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), cob(I)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.CPD-20905). Products: Triphosphate (molecule.C00536), adenosylcob(III)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.B12-Corrinoid-Adenosyltranferase).

## Enriched Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Annotation

This reaction synthesizes adenosylcobalamin.

## Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A9H5|protein.P0A9H5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.B12-Corrinoid-Adenosyltranferase|molecule.ecocyc.B12-Corrinoid-Adenosyltranferase]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20905|molecule.ecocyc.CPD-20905]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:COBALADENOSYLTRANS-RXN`

## Notes

CPD-20905 + ATP + PROTON -> B12-Corrinoid-Adenosyltranferase + P3I; direction=PHYSIOL-LEFT-TO-RIGHT
