---
entity_id: "reaction.ecocyc.TRANS-RXN-281"
entity_type: "reaction"
name: "L-isoleucine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-isoleucine:proton antiport

`reaction.ecocyc.TRANS-RXN-281`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-281`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ILE + PROTON -> ILE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: ILE + PROTON -> ILE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by yjeH (protein.P39277). Substrates: H+ (molecule.C00080), L-Isoleucine (molecule.C00407). Products: H+ (molecule.C00080), L-Isoleucine (molecule.C00407).

## Annotation

ILE + PROTON -> ILE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-281`

## Notes

ILE + PROTON -> ILE + PROTON; direction=REVERSIBLE
