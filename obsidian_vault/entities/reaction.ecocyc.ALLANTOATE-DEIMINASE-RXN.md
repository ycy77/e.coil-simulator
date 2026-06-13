---
entity_id: "reaction.ecocyc.ALLANTOATE-DEIMINASE-RXN"
entity_type: "reaction"
name: "ALLANTOATE-DEIMINASE-RXN"
source_database: "EcoCyc"
source_id: "ALLANTOATE-DEIMINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALLANTOATE-DEIMINASE-RXN

`reaction.ecocyc.ALLANTOATE-DEIMINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALLANTOATE-DEIMINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + ALLANTOATE + WATER -> CPD0-2298 + AMMONIUM + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + ALLANTOATE + WATER -> CPD0-2298 + AMMONIUM + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by allantoate amidohydrolase (complex.ecocyc.CPLX-7524). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Allantoate (molecule.C00499). Products: CO2 (molecule.C00011), (S)-Ureidoglycine (molecule.C02091), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Annotation

PROTON + ALLANTOATE + WATER -> CPD0-2298 + AMMONIUM + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX-7524|complex.ecocyc.CPLX-7524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02091|molecule.C02091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00499|molecule.C00499]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALLANTOATE-DEIMINASE-RXN`

## Notes

PROTON + ALLANTOATE + WATER -> CPD0-2298 + AMMONIUM + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
