---
entity_id: "reaction.ecocyc.TRANS-RXN0-444"
entity_type: "reaction"
name: "TRANS-RXN0-444"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-444

`reaction.ecocyc.TRANS-RXN0-444`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-444`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli is able to use S-allantoin as a sole nitrogen source under anaerobic conditions EcoCyc reaction equation: S-ALLANTOIN + PROTON -> S-ALLANTOIN + PROTON; direction=LEFT-TO-RIGHT. E. coli is able to use S-allantoin as a sole nitrogen source under anaerobic conditions

## Biological Role

Catalyzed by ybbW (protein.P75712). Substrates: H+ (molecule.C00080), (S)-Allantoin (molecule.C02350). Products: H+ (molecule.C00080), (S)-Allantoin (molecule.C02350).

## Enriched Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Annotation

E. coli is able to use S-allantoin as a sole nitrogen source under anaerobic conditions

## Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[protein.P77671|protein.P77671]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P75712|protein.P75712]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02350|molecule.C02350]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02350|molecule.C02350]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-444`

## Notes

S-ALLANTOIN + PROTON -> S-ALLANTOIN + PROTON; direction=LEFT-TO-RIGHT
