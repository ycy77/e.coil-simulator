---
entity_id: "reaction.ecocyc.RXN-18708"
entity_type: "reaction"
name: "RXN-18708"
source_database: "EcoCyc"
source_id: "RXN-18708"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18708

`reaction.ecocyc.RXN-18708`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18708`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TusD-Persulfides + TusE-L-cysteine -> TusD-L-cysteine + TusE-S-sulfanylcysteine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TusD-Persulfides + TusE-L-cysteine -> TusD-L-cysteine + TusE-S-sulfanylcysteine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sulfurtransferase complex TusBCD (complex.ecocyc.CPLX-3942). Substrates: a [TusD sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.TusD-Persulfides), a [TusE sulfur carrier protein]-L-cysteine (molecule.ecocyc.TusE-L-cysteine). Products: a [TusD]-L-cysteine (molecule.ecocyc.TusD-L-cysteine), a [TusE sulfur carrier protein]-S-sulfanylcysteine (molecule.ecocyc.TusE-S-sulfanylcysteine).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

TusD-Persulfides + TusE-L-cysteine -> TusD-L-cysteine + TusE-S-sulfanylcysteine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-3942|complex.ecocyc.CPLX-3942]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.TusD-L-cysteine|molecule.ecocyc.TusD-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TusE-S-sulfanylcysteine|molecule.ecocyc.TusE-S-sulfanylcysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.TusD-Persulfides|molecule.ecocyc.TusD-Persulfides]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TusE-L-cysteine|molecule.ecocyc.TusE-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18708`

## Notes

TusD-Persulfides + TusE-L-cysteine -> TusD-L-cysteine + TusE-S-sulfanylcysteine; direction=PHYSIOL-LEFT-TO-RIGHT
