---
entity_id: "reaction.ecocyc.ISOCIT-CLEAV-RXN"
entity_type: "reaction"
name: "ISOCIT-CLEAV-RXN"
source_database: "EcoCyc"
source_id: "ISOCIT-CLEAV-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "glyoxylate-succinate condensation"
  - "isocitrate cleavage"
---

# ISOCIT-CLEAV-RXN

`reaction.ecocyc.ISOCIT-CLEAV-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ISOCIT-CLEAV-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reaction cleaves isocitrate in one direction, condenses glyoxalate and succinate in the other direction EcoCyc reaction equation: THREO-DS-ISO-CITRATE -> GLYOX + SUC; direction=REVERSIBLE. The reaction cleaves isocitrate in one direction, condenses glyoxalate and succinate in the other direction

## Biological Role

Catalyzed by isocitrate lyase (complex.ecocyc.ISOCIT-LYASE). Substrates: D-threo-isocitrate (molecule.ecocyc.THREO-DS-ISO-CITRATE). Products: Succinate (molecule.C00042), Glyoxylate (molecule.C00048).

## Enriched Pathways

- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)

## Annotation

The reaction cleaves isocitrate in one direction, condenses glyoxalate and succinate in the other direction

## Pathways

- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (22)

- `catalyzes` <-- [[complex.ecocyc.ISOCIT-LYASE|complex.ecocyc.ISOCIT-LYASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.THREO-DS-ISO-CITRATE|molecule.ecocyc.THREO-DS-ISO-CITRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00383|molecule.C00383]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00417|molecule.C00417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00490|molecule.C00490]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02170|molecule.C02170]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05669|molecule.C05669]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9275|molecule.ecocyc.CPD-9275]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HYDROXYMALONATE|molecule.ecocyc.HYDROXYMALONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ISOCIT-CLEAV-RXN`

## Notes

THREO-DS-ISO-CITRATE -> GLYOX + SUC; direction=REVERSIBLE
