---
entity_id: "reaction.ecocyc.ASPARTASE-RXN"
entity_type: "reaction"
name: "ASPARTASE-RXN"
source_database: "EcoCyc"
source_id: "ASPARTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPARTASE-RXN

`reaction.ecocyc.ASPARTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the reversible deamination of L-aspartate to form fumarate and ammonia EcoCyc reaction equation: L-ASPARTATE -> AMMONIUM + FUM; direction=REVERSIBLE. This reaction is the reversible deamination of L-aspartate to form fumarate and ammonia

## Biological Role

Catalyzed by aspartate ammonia-lyase (complex.ecocyc.ASPARTASE-CPLX). Substrates: L-Aspartate (molecule.C00049). Products: Fumarate (molecule.C00122), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.ASPASN-PWY` superpathway of L-aspartate and L-asparagine biosynthesis (EcoCyc)
- `ecocyc.GLUTDEG-PWY` L-glutamate degradation II (EcoCyc)
- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)
- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Annotation

This reaction is the reversible deamination of L-aspartate to form fumarate and ammonia

## Pathways

- `ecocyc.ASPASN-PWY` superpathway of L-aspartate and L-asparagine biosynthesis (EcoCyc)
- `ecocyc.GLUTDEG-PWY` L-glutamate degradation II (EcoCyc)
- `ecocyc.PWY-8291` L-aspartate degradation II (aerobic) (EcoCyc)
- `ecocyc.PWY-8294` L-aspartate degradation III (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[complex.ecocyc.PIIPROTEIN-CPLX|complex.ecocyc.PIIPROTEIN-CPLX]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1614|molecule.ecocyc.CPD0-1614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ASPARTASE-CPLX|complex.ecocyc.ASPARTASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00441|molecule.C00441]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05672|molecule.C05672]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3722|molecule.ecocyc.CPD-3722]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1616|molecule.ecocyc.CPD0-1616]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPARTASE-RXN`

## Notes

L-ASPARTATE -> AMMONIUM + FUM; direction=REVERSIBLE
