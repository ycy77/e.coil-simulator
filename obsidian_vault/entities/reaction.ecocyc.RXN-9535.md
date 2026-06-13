---
entity_id: "reaction.ecocyc.RXN-9535"
entity_type: "reaction"
name: "RXN-9535"
source_database: "EcoCyc"
source_id: "RXN-9535"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9535

`reaction.ecocyc.RXN-9535`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9535`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-myristoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Dodecanoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-myristoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Dodecanoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-myristoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9535`

## Notes

Dodecanoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-myristoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT
