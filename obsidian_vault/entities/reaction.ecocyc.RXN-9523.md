---
entity_id: "reaction.ecocyc.RXN-9523"
entity_type: "reaction"
name: "3-oxo-octanoyl-[acyl-carrier protein] synthase"
source_database: "EcoCyc"
source_id: "RXN-9523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-oxo-octanoyl-[acyl-carrier protein] synthase

`reaction.ecocyc.RXN-9523`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9523`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hexanoyl-ACPs + MALONYL-ACP + PROTON -> 3-Oxo-octanoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Hexanoyl-ACPs + MALONYL-ACP + PROTON -> 3-Oxo-octanoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Hexanoyl-ACPs + MALONYL-ACP + PROTON -> 3-Oxo-octanoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9523`

## Notes

Hexanoyl-ACPs + MALONYL-ACP + PROTON -> 3-Oxo-octanoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT
