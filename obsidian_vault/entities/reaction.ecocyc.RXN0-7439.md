---
entity_id: "reaction.ecocyc.RXN0-7439"
entity_type: "reaction"
name: "RXN0-7439"
source_database: "EcoCyc"
source_id: "RXN0-7439"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7439

`reaction.ecocyc.RXN0-7439`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7439`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + SufE-L-cysteine -> L-ALPHA-ALANINE + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + SufE-L-cysteine -> L-ALPHA-ALANINE + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-cysteine desulfurase SufS (complex.ecocyc.CPLX0-246). Substrates: L-Cysteine (molecule.C00097), a [SufE sulfur-carrier protein]-L-cysteine (molecule.ecocyc.SufE-L-cysteine). Products: L-Alanine (molecule.C00041), a [SufE sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufE-L-cysteine-Persulfide).

## Annotation

CYS + SufE-L-cysteine -> L-ALPHA-ALANINE + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.ecocyc.SufE-L-cysteine|molecule.ecocyc.SufE-L-cysteine]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-246|complex.ecocyc.CPLX0-246]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SufE-L-cysteine-Persulfide|molecule.ecocyc.SufE-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SufE-L-cysteine|molecule.ecocyc.SufE-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7439`

## Notes

CYS + SufE-L-cysteine -> L-ALPHA-ALANINE + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
