---
entity_id: "reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN"
entity_type: "reaction"
name: "PHENYLSERINE-ALDOLASE-RXN"
source_database: "EcoCyc"
source_id: "PHENYLSERINE-ALDOLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHENYLSERINE-ALDOLASE-RXN

`reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHENYLSERINE-ALDOLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-644 -> BENZALDEHYDE + GLY; direction=REVERSIBLE EcoCyc reaction equation: CPD-644 -> BENZALDEHYDE + GLY; direction=REVERSIBLE.

## Biological Role

Catalyzed by low-specificity L-threonine aldolase (complex.ecocyc.LTAA-CPLX). Substrates: L-threo-3-phenylserine (molecule.ecocyc.CPD-644). Products: Glycine (molecule.C00037), Benzaldehyde (molecule.C00261).

## Annotation

CPD-644 -> BENZALDEHYDE + GLY; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.ecocyc.CPD-8855|molecule.ecocyc.CPD-8855]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00261|molecule.C00261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-644|molecule.ecocyc.CPD-644]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHENYLSERINE-ALDOLASE-RXN`

## Notes

CPD-644 -> BENZALDEHYDE + GLY; direction=REVERSIBLE
