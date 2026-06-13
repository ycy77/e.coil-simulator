---
entity_id: "reaction.ecocyc.RXN0-7437"
entity_type: "reaction"
name: "RXN0-7437"
source_database: "EcoCyc"
source_id: "RXN0-7437"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7437

`reaction.ecocyc.RXN0-7437`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7437`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SufS-L-cysteine-Persulfide + SufE-L-cysteine -> SufS-L-cysteine + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SufS-L-cysteine-Persulfide + SufE-L-cysteine -> SufS-L-cysteine + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [SufE sulfur-carrier protein]-L-cysteine (molecule.ecocyc.SufE-L-cysteine), a [SufS L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufS-L-cysteine-Persulfide). Products: a [SufE sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufE-L-cysteine-Persulfide), a [SufS]-L-cysteine (molecule.ecocyc.SufS-L-cysteine).

## Annotation

SufS-L-cysteine-Persulfide + SufE-L-cysteine -> SufS-L-cysteine + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.SufE-L-cysteine-Persulfide|molecule.ecocyc.SufE-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SufS-L-cysteine|molecule.ecocyc.SufS-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.SufE-L-cysteine|molecule.ecocyc.SufE-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SufS-L-cysteine-Persulfide|molecule.ecocyc.SufS-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7437`

## Notes

SufS-L-cysteine-Persulfide + SufE-L-cysteine -> SufS-L-cysteine + SufE-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
