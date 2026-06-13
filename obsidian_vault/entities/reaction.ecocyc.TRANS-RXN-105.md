---
entity_id: "reaction.ecocyc.TRANS-RXN-105"
entity_type: "reaction"
name: "glycolate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-105"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycolate:proton symport

`reaction.ecocyc.TRANS-RXN-105`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-105`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + GLYCOLLATE -> PROTON + GLYCOLLATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + GLYCOLLATE -> PROTON + GLYCOLLATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by lldP (protein.P33231), glcA (protein.Q46839). Substrates: H+ (molecule.C00080), Glycolate (molecule.C00160). Products: H+ (molecule.C00080), Glycolate (molecule.C00160).

## Annotation

PROTON + GLYCOLLATE -> PROTON + GLYCOLLATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33231|protein.P33231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-105`

## Notes

PROTON + GLYCOLLATE -> PROTON + GLYCOLLATE; direction=REVERSIBLE
