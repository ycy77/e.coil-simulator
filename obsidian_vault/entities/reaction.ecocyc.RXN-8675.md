---
entity_id: "reaction.ecocyc.RXN-8675"
entity_type: "reaction"
name: "RXN-8675"
source_database: "EcoCyc"
source_id: "RXN-8675"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8675

`reaction.ecocyc.RXN-8675`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8675`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD-9038 -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-9038 -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), precorrin-1 (molecule.ecocyc.CPD-9038). Products: S-Adenosyl-L-homocysteine (molecule.C00021), Precorrin 2 (molecule.C02463).

## Enriched Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + CPD-9038 -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02463|molecule.C02463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9038|molecule.ecocyc.CPD-9038]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8675`

## Notes

S-ADENOSYLMETHIONINE + CPD-9038 -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN; direction=PHYSIOL-LEFT-TO-RIGHT
