---
entity_id: "reaction.ecocyc.NAPHTHOATE-SYN-RXN"
entity_type: "reaction"
name: "NAPHTHOATE-SYN-RXN"
source_database: "EcoCyc"
source_id: "NAPHTHOATE-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NAPHTHOATE-SYN-RXN

`reaction.ecocyc.NAPHTHOATE-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAPHTHOATE-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth reaction in menaquinone biosynthesis. EcoCyc reaction equation: PROTON + CPD-6972 -> CPD-9925 + WATER; direction=LEFT-TO-RIGHT. This is the fifth reaction in menaquinone biosynthesis.

## Biological Role

Catalyzed by 1,4-dihydroxy-2-naphthoyl-CoA synthase (complex.ecocyc.CPLX0-7882). Substrates: H+ (molecule.C00080), 2-Succinylbenzoyl-CoA (molecule.C03160). Products: H2O (molecule.C00001), 1,4-Dihydroxy-2-naphthoyl-CoA (molecule.C15547).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

This is the fifth reaction in menaquinone biosynthesis.

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7882|complex.ecocyc.CPLX0-7882]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15547|molecule.C15547]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03160|molecule.C03160]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C15547|molecule.C15547]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NAPHTHOATE-SYN-RXN`

## Notes

PROTON + CPD-6972 -> CPD-9925 + WATER; direction=LEFT-TO-RIGHT
