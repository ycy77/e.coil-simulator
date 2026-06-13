---
entity_id: "reaction.ecocyc.CARBAMATE-KINASE-RXN"
entity_type: "reaction"
name: "CARBAMATE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "CARBAMATE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CARBAMATE-KINASE-RXN

`reaction.ecocyc.CARBAMATE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARBAMATE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMMONIUM + HCO3 + ATP -> CARBAMOYL-P + ADP + WATER + PROTON; direction=REVERSIBLE EcoCyc reaction equation: AMMONIUM + HCO3 + ATP -> CARBAMOYL-P + ADP + WATER + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by allK (protein.P37306). Substrates: ATP (molecule.C00002), HCO3- (molecule.C00288), ammonium (molecule.ecocyc.AMMONIUM). Products: H2O (molecule.C00001), ADP (molecule.C00008), H+ (molecule.C00080), Carbamoyl phosphate (molecule.C00169).

## Annotation

AMMONIUM + HCO3 + ATP -> CARBAMOYL-P + ADP + WATER + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37306|protein.P37306]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CARBAMATE-KINASE-RXN`

## Notes

AMMONIUM + HCO3 + ATP -> CARBAMOYL-P + ADP + WATER + PROTON; direction=REVERSIBLE
