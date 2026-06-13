---
entity_id: "reaction.ecocyc.RXN-14932"
entity_type: "reaction"
name: "RXN-14932"
source_database: "EcoCyc"
source_id: "RXN-14932"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14932

`reaction.ecocyc.RXN-14932`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14932`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

R-2-HYDROXYGLUTARATE + Acceptor -> 2-KETOGLUTARATE + Donor-H2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: R-2-HYDROXYGLUTARATE + Acceptor -> 2-KETOGLUTARATE + Donor-H2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-2-hydroxyglutarate dehydrogenase (complex.ecocyc.CPLX0-9749). Substrates: (R)-2-Hydroxyglutarate (molecule.C01087). Products: 2-Oxoglutarate (molecule.C00026).

## Enriched Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Annotation

R-2-HYDROXYGLUTARATE + Acceptor -> 2-KETOGLUTARATE + Donor-H2; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-9749|complex.ecocyc.CPLX0-9749]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01087|molecule.C01087]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14932`

## Notes

R-2-HYDROXYGLUTARATE + Acceptor -> 2-KETOGLUTARATE + Donor-H2; direction=LEFT-TO-RIGHT
