---
entity_id: "reaction.ecocyc.RXN0-5222"
entity_type: "reaction"
name: "cyanase"
source_database: "EcoCyc"
source_id: "RXN0-5222"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cyanase

`reaction.ecocyc.RXN0-5222`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5222`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBAMATE + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CARBAMATE + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative aminoacrylate hydrolase RutD (complex.ecocyc.CPLX0-8303). Substrates: H+ (molecule.C00080), Carbamate (molecule.C01563). Products: CO2 (molecule.C00011), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)
- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Annotation

CARBAMATE + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)
- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8303|complex.ecocyc.CPLX0-8303]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5222`

## Notes

CARBAMATE + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
