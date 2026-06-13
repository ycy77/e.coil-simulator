---
entity_id: "reaction.ecocyc.DIACYLGLYKIN-RXN"
entity_type: "reaction"
name: "DIACYLGLYKIN-RXN"
source_database: "EcoCyc"
source_id: "DIACYLGLYKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIACYLGLYKIN-RXN

`reaction.ecocyc.DIACYLGLYKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIACYLGLYKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction recycles diacylglycerol which is generated during MDO biosynthesis. EcoCyc reaction equation: ATP + DIACYLGLYCEROL -> PROTON + L-PHOSPHATIDATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction recycles diacylglycerol which is generated during MDO biosynthesis.

## Biological Role

Catalyzed by diacylglycerol kinase (complex.ecocyc.DIACYLGLYKIN-CPLX). Substrates: ATP (molecule.C00002), 1,2-Diacyl-sn-glycerol (molecule.C00641). Products: ADP (molecule.C00008), H+ (molecule.C00080), Phosphatidate (molecule.C00416).

## Annotation

This reaction recycles diacylglycerol which is generated during MDO biosynthesis.

## Outgoing Edges (0)

_None._

## Incoming Edges (23)

- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.DIACYLGLYKIN-CPLX|complex.ecocyc.DIACYLGLYKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1759|molecule.ecocyc.CPD0-1759]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1760|molecule.ecocyc.CPD0-1760]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1761|molecule.ecocyc.CPD0-1761]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1762|molecule.ecocyc.CPD0-1762]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1763|molecule.ecocyc.CPD0-1763]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1807|molecule.ecocyc.CPD0-1807]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1808|molecule.ecocyc.CPD0-1808]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1809|molecule.ecocyc.CPD0-1809]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1810|molecule.ecocyc.CPD0-1810]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1811|molecule.ecocyc.CPD0-1811]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1812|molecule.ecocyc.CPD0-1812]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1815|molecule.ecocyc.CPD0-1815]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1816|molecule.ecocyc.CPD0-1816]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIACYLGLYKIN-RXN`

## Notes

ATP + DIACYLGLYCEROL -> PROTON + L-PHOSPHATIDATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
