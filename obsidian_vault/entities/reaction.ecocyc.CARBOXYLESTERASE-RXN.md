---
entity_id: "reaction.ecocyc.CARBOXYLESTERASE-RXN"
entity_type: "reaction"
name: "CARBOXYLESTERASE-RXN"
source_database: "EcoCyc"
source_id: "CARBOXYLESTERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Ali-esterase"
  - "Monobutyrase"
  - "Cocaine esterase"
  - "Procaine esterase"
  - "Methylbutyrase"
---

# CARBOXYLESTERASE-RXN

`reaction.ecocyc.CARBOXYLESTERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARBOXYLESTERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Carboxylic-esters + WATER -> Alcohols + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Carboxylic-esters + WATER -> Alcohols + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by carboxylesterase (complex.ecocyc.CPLX0-8214), bioH (protein.P13001). Substrates: H2O (molecule.C00001), a carboxylic ester (molecule.ecocyc.Carboxylic-esters). Products: H+ (molecule.C00080), an alcohol (molecule.ecocyc.Alcohols), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

Carboxylic-esters + WATER -> Alcohols + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8214|complex.ecocyc.CPLX0-8214]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P13001|protein.P13001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Carboxylic-esters|molecule.ecocyc.Carboxylic-esters]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CARBOXYLESTERASE-RXN`

## Notes

Carboxylic-esters + WATER -> Alcohols + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
