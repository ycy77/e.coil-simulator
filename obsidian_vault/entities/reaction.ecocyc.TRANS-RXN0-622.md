---
entity_id: "reaction.ecocyc.TRANS-RXN0-622"
entity_type: "reaction"
name: "hydroxybutanoate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-622"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydroxybutanoate:proton symport

`reaction.ecocyc.TRANS-RXN0-622`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-622`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-3564 + PROTON -> CPD-3564 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-3564 + PROTON -> CPD-3564 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by lldP (protein.P33231), glcA (protein.Q46839). Substrates: H+ (molecule.C00080), 2-Hydroxybutanoic acid (molecule.C05984). Products: H+ (molecule.C00080), 2-Hydroxybutanoic acid (molecule.C05984).

## Annotation

CPD-3564 + PROTON -> CPD-3564 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33231|protein.P33231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05984|molecule.C05984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05984|molecule.C05984]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-622`

## Notes

CPD-3564 + PROTON -> CPD-3564 + PROTON; direction=REVERSIBLE
