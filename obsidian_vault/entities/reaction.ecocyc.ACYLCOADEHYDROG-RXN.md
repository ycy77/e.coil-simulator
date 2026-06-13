---
entity_id: "reaction.ecocyc.ACYLCOADEHYDROG-RXN"
entity_type: "reaction"
name: "ACYLCOADEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "ACYLCOADEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACYLCOADEHYDROG-RXN

`reaction.ecocyc.ACYLCOADEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACYLCOADEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in fatty acid degradation and part of the β-oxidation cycle. EcoCyc reaction equation: Saturated-Fatty-Acyl-CoA + ETF-Oxidized + PROTON -> TRANS-D2-ENOYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT. The second step in fatty acid degradation and part of the β-oxidation cycle.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA). Products: a (2E)-2-enoyl-CoA (molecule.ecocyc.TRANS-D2-ENOYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

The second step in fatty acid degradation and part of the β-oxidation cycle.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.TRANS-D2-ENOYL-COA|molecule.ecocyc.TRANS-D2-ENOYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACYLCOADEHYDROG-RXN`

## Notes

Saturated-Fatty-Acyl-CoA + ETF-Oxidized + PROTON -> TRANS-D2-ENOYL-COA + ETF-Reduced; direction=PHYSIOL-LEFT-TO-RIGHT
