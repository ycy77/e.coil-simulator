---
entity_id: "reaction.ecocyc.RXN-12876"
entity_type: "reaction"
name: "RXN-12876"
source_database: "EcoCyc"
source_id: "RXN-12876"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12876

`reaction.ecocyc.RXN-12876`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12876`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASCORBATE + Cytochromes-C-Oxidized -> L-DEHYDRO-ASCORBATE + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASCORBATE + Cytochromes-C-Oxidized -> L-DEHYDRO-ASCORBATE + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Ascorbate (molecule.C00072). Products: H+ (molecule.C00080), Dehydroascorbate (molecule.C05422).

## Annotation

ASCORBATE + Cytochromes-C-Oxidized -> L-DEHYDRO-ASCORBATE + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12876`

## Notes

ASCORBATE + Cytochromes-C-Oxidized -> L-DEHYDRO-ASCORBATE + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
