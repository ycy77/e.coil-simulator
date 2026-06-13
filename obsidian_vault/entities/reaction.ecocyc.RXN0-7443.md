---
entity_id: "reaction.ecocyc.RXN0-7443"
entity_type: "reaction"
name: "RXN0-7443"
source_database: "EcoCyc"
source_id: "RXN0-7443"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7443

`reaction.ecocyc.RXN0-7443`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7443`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SufE-L-cysteine-Persulfide + SufB-L-cysteine -> SufE-L-cysteine + SufB-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SufE-L-cysteine-Persulfide + SufB-L-cysteine -> SufE-L-cysteine + SufB-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sufE (protein.P76194). Substrates: a [SufB Fe-S cluster scaffold protein]-L-cysteine (molecule.ecocyc.SufB-L-cysteine), a [SufE sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufE-L-cysteine-Persulfide). Products: a [SufB Fe-S cluster scaffold protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.SufB-L-cysteine-Persulfide), a [SufE sulfur-carrier protein]-L-cysteine (molecule.ecocyc.SufE-L-cysteine).

## Annotation

SufE-L-cysteine-Persulfide + SufB-L-cysteine -> SufE-L-cysteine + SufB-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76194|protein.P76194]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.SufB-L-cysteine-Persulfide|molecule.ecocyc.SufB-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SufE-L-cysteine|molecule.ecocyc.SufE-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.SufB-L-cysteine|molecule.ecocyc.SufB-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SufE-L-cysteine-Persulfide|molecule.ecocyc.SufE-L-cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7443`

## Notes

SufE-L-cysteine-Persulfide + SufB-L-cysteine -> SufE-L-cysteine + SufB-L-cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
