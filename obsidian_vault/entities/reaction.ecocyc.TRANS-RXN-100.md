---
entity_id: "reaction.ecocyc.TRANS-RXN-100"
entity_type: "reaction"
name: "L-carnitine:γ-butyrobetaine antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-100"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-carnitine:γ-butyrobetaine antiport

`reaction.ecocyc.TRANS-RXN-100`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-100`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GAMMA-BUTYROBETAINE + CARNITINE -> GAMMA-BUTYROBETAINE + CARNITINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GAMMA-BUTYROBETAINE + CARNITINE -> GAMMA-BUTYROBETAINE + CARNITINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-carnitine:γ-butyrobetaine antiporter (complex.ecocyc.CPLX0-7906). Substrates: 4-Trimethylammoniobutanoate (molecule.C01181), L-carnitine (molecule.ecocyc.CARNITINE). Products: 4-Trimethylammoniobutanoate (molecule.C01181), L-carnitine (molecule.ecocyc.CARNITINE).

## Enriched Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Annotation

GAMMA-BUTYROBETAINE + CARNITINE -> GAMMA-BUTYROBETAINE + CARNITINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7906|complex.ecocyc.CPLX0-7906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-100`

## Notes

GAMMA-BUTYROBETAINE + CARNITINE -> GAMMA-BUTYROBETAINE + CARNITINE; direction=LEFT-TO-RIGHT
