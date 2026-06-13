---
entity_id: "reaction.ecocyc.RXN0-2941"
entity_type: "reaction"
name: "RXN0-2941"
source_database: "EcoCyc"
source_id: "RXN0-2941"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2941

`reaction.ecocyc.RXN0-2941`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2941`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-With-Recognition-Site + WATER + GTP -> Cleaved-DNA + GDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-With-Recognition-Site + WATER + GTP -> Cleaved-DNA + GDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by McrBC restriction endonuclease (complex.ecocyc.CPLX0-2661). Substrates: H2O (molecule.C00001), GTP (molecule.C00044), DNA containing a recognition site (molecule.ecocyc.DNA-With-Recognition-Site). Products: GDP (molecule.C00035), cleaved DNA (molecule.ecocyc.Cleaved-DNA), phosphate (molecule.ecocyc.Pi).

## Annotation

DNA-With-Recognition-Site + WATER + GTP -> Cleaved-DNA + GDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2661|complex.ecocyc.CPLX0-2661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Cleaved-DNA|molecule.ecocyc.Cleaved-DNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-With-Recognition-Site|molecule.ecocyc.DNA-With-Recognition-Site]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2941`

## Notes

DNA-With-Recognition-Site + WATER + GTP -> Cleaved-DNA + GDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
