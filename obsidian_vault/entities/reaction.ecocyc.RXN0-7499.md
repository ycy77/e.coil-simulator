---
entity_id: "reaction.ecocyc.RXN0-7499"
entity_type: "reaction"
name: "phosphotidylhomoserine synthase"
source_database: "EcoCyc"
source_id: "RXN0-7499"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phosphotidylhomoserine synthase

`reaction.ecocyc.RXN0-7499`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7499`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction occurs in E. coli when grown in minimal media . EcoCyc reaction equation: CDPDIACYLGLYCEROL + HOMO-SER -> CPD0-2733 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction occurs in E. coli when grown in minimal media .

## Biological Role

Catalyzed by phosphatidylserine synthase (complex.ecocyc.CPLX0-12524). Substrates: L-Homoserine (molecule.C00263), CDP-diacylglycerol (molecule.C00269). Products: CMP (molecule.C00055), H+ (molecule.C00080), a phosphatidylhomoserine (molecule.ecocyc.CPD0-2733).

## Enriched Pathways

- `ecocyc.PWY0-1644` phosphatidylhomoserine and phosphatidylpropanolamine biosynthesis (EcoCyc)

## Annotation

This reaction occurs in E. coli when grown in minimal media .

## Pathways

- `ecocyc.PWY0-1644` phosphatidylhomoserine and phosphatidylpropanolamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12524|complex.ecocyc.CPLX0-12524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2733|molecule.ecocyc.CPD0-2733]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7499`

## Notes

CDPDIACYLGLYCEROL + HOMO-SER -> CPD0-2733 + CMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
