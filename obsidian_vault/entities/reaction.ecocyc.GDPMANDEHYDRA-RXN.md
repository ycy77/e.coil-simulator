---
entity_id: "reaction.ecocyc.GDPMANDEHYDRA-RXN"
entity_type: "reaction"
name: "GDPMANDEHYDRA-RXN"
source_database: "EcoCyc"
source_id: "GDPMANDEHYDRA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDPMANDEHYDRA-RXN

`reaction.ecocyc.GDPMANDEHYDRA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDPMANDEHYDRA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the biosynthetic pathway of GDP-L-fucose, a precursor of colanic acid. EcoCyc reaction equation: GDP-MANNOSE -> WATER + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in the biosynthetic pathway of GDP-L-fucose, a precursor of colanic acid.

## Biological Role

Catalyzed by GDP-mannose 4,6-dehydratase (complex.ecocyc.GDPMANDEHYDRA-CPLX). Substrates: GDP-mannose (molecule.C00096). Products: H2O (molecule.C00001), GDP-4-dehydro-6-deoxy-D-mannose (molecule.C01222).

## Enriched Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Annotation

This is a reaction in the biosynthetic pathway of GDP-L-fucose, a precursor of colanic acid.

## Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GDPMANDEHYDRA-CPLX|complex.ecocyc.GDPMANDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01222|molecule.C01222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00096|molecule.C00096]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00325|molecule.C00325]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00394|molecule.C00394]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GDPMANDEHYDRA-RXN`

## Notes

GDP-MANNOSE -> WATER + GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE; direction=PHYSIOL-LEFT-TO-RIGHT
