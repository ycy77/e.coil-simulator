---
entity_id: "reaction.ecocyc.TRANS-RXN0-628"
entity_type: "reaction"
name: "xenobiotic:proton antiport (electrogenic)"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-628"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xenobiotic:proton antiport (electrogenic)

`reaction.ecocyc.TRANS-RXN0-628`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-628`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Xenobiotic + PROTON -> Xenobiotic + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Xenobiotic + PROTON -> Xenobiotic + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963). Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

Xenobiotic + PROTON -> Xenobiotic + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-628`

## Notes

Xenobiotic + PROTON -> Xenobiotic + PROTON; direction=LEFT-TO-RIGHT
