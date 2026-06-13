---
entity_id: "reaction.ecocyc.RXN0-7050"
entity_type: "reaction"
name: "L-methionine:proton antiport"
source_database: "EcoCyc"
source_id: "RXN0-7050"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-methionine:proton antiport

`reaction.ecocyc.RXN0-7050`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7050`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + MET -> PROTON + MET; direction=REVERSIBLE EcoCyc reaction equation: PROTON + MET -> PROTON + MET; direction=REVERSIBLE.

## Biological Role

Catalyzed by yjeH (protein.P39277), leuE (protein.P76249). Substrates: L-Methionine (molecule.C00073), H+ (molecule.C00080). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080).

## Annotation

PROTON + MET -> PROTON + MET; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76249|protein.P76249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7050`

## Notes

PROTON + MET -> PROTON + MET; direction=REVERSIBLE
