---
entity_id: "reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN"
entity_type: "reaction"
name: "GLYCOLALD-DEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "GLYCOLALD-DEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOLALD-DEHYDROG-RXN

`reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOLALD-DEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycolate is catabolized via glycolaldehyde to glycolate. EcoCyc reaction equation: WATER + NAD + GLYCOLALDEHYDE -> PROTON + NADH + GLYCOLLATE; direction=LEFT-TO-RIGHT. Glycolate is catabolized via glycolaldehyde to glycolate.

## Biological Role

Catalyzed by aldehyde dehydrogenase A, NAD-linked (complex.ecocyc.ALD-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Glycolaldehyde (molecule.C00266). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glycolate (molecule.C00160).

## Enriched Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)
- `ecocyc.PWY0-1280` ethylene glycol degradation (EcoCyc)

## Annotation

Glycolate is catabolized via glycolaldehyde to glycolate.

## Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)
- `ecocyc.PWY0-1280` ethylene glycol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ALD-CPLX|complex.ecocyc.ALD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCOLALD-DEHYDROG-RXN`

## Notes

WATER + NAD + GLYCOLALDEHYDE -> PROTON + NADH + GLYCOLLATE; direction=LEFT-TO-RIGHT
