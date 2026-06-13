---
entity_id: "reaction.ecocyc.PFLDEACTIV-RXN"
entity_type: "reaction"
name: "PFLDEACTIV-RXN"
source_database: "EcoCyc"
source_id: "PFLDEACTIV-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PFLDEACTIV-RXN

`reaction.ecocyc.PFLDEACTIV-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PFLDEACTIV-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction deactivates the pyruvate formate-lyase enzyme. EcoCyc reaction equation: PYRUVFORMLY-MONOMER -> PYRUVFORMLY-INACTIVE-CPLX; direction=. This reaction deactivates the pyruvate formate-lyase enzyme.

## Biological Role

Catalyzed by fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase (complex.ecocyc.ADHE-CPLX).

## Annotation

This reaction deactivates the pyruvate formate-lyase enzyme.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.ADHE-CPLX|complex.ecocyc.ADHE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1889|molecule.ecocyc.CPD0-1889]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PFLDEACTIV-RXN`

## Notes

PYRUVFORMLY-MONOMER -> PYRUVFORMLY-INACTIVE-CPLX; direction=
