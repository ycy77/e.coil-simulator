---
entity_id: "reaction.ecocyc.RXN-10654"
entity_type: "reaction"
name: "RXN-10654"
source_database: "EcoCyc"
source_id: "RXN-10654"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10654

`reaction.ecocyc.RXN-10654`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10654`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cis-Delta5-dodecenoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-D7-tetradecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Cis-Delta5-dodecenoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-D7-tetradecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-6282` palmitoleate biosynthesis I (from (5Z)-dodec-5-enoate) (EcoCyc)

## Annotation

Cis-Delta5-dodecenoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-D7-tetradecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6282` palmitoleate biosynthesis I (from (5Z)-dodec-5-enoate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10654`

## Notes

Cis-Delta5-dodecenoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-D7-tetradecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
