---
entity_id: "reaction.ecocyc.SELENOCYSTEINE-LYASE-RXN"
entity_type: "reaction"
name: "SELENOCYSTEINE-LYASE-RXN"
source_database: "EcoCyc"
source_id: "SELENOCYSTEINE-LYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "SELENOCYSTEINE REDUCTASE"
---

# SELENOCYSTEINE-LYASE-RXN

`reaction.ecocyc.SELENOCYSTEINE-LYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SELENOCYSTEINE-LYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Donor-H2 + L-SELENOCYSTEINE -> L-ALPHA-ALANINE + SE-2 + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Donor-H2 + L-SELENOCYSTEINE -> L-ALPHA-ALANINE + SE-2 + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Selenocysteine (molecule.C05688). Products: L-Alanine (molecule.C00041), H+ (molecule.C00080), selenide (molecule.ecocyc.SE-2).

## Annotation

Donor-H2 + L-SELENOCYSTEINE -> L-ALPHA-ALANINE + SE-2 + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SE-2|molecule.ecocyc.SE-2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05688|molecule.C05688]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SELENOCYSTEINE-LYASE-RXN`

## Notes

Donor-H2 + L-SELENOCYSTEINE -> L-ALPHA-ALANINE + SE-2 + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
