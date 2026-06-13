---
entity_id: "reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN"
entity_type: "reaction"
name: "3-HYDROXYDECANOYL-ACP-DEHYDR-RXN"
source_database: "EcoCyc"
source_id: "3-HYDROXYDECANOYL-ACP-DEHYDR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-HYDROXYDECANOYL-ACP-DEHYDR-RXN

`reaction.ecocyc.3-HYDROXYDECANOYL-ACP-DEHYDR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-HYDROXYDECANOYL-ACP-DEHYDR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A key step in the anaerobic pathway of unsaturated fatty acid synthesis. EcoCyc reaction equation: OH-ACYL-ACP -> TRANS-D2-ENOYL-ACP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. A key step in the anaerobic pathway of unsaturated fatty acid synthesis.

## Biological Role

Catalyzed by β-hydroxyacyl-acyl carrier protein dehydratase/isomerase (complex.ecocyc.FABA-CPLX), 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Annotation

A key step in the anaerobic pathway of unsaturated fatty acid synthesis.

## Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.FABA-CPLX|complex.ecocyc.FABA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` <-- [[molecule.ecocyc.CPD0-1306|molecule.ecocyc.CPD0-1306]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-HYDROXYDECANOYL-ACP-DEHYDR-RXN`

## Notes

OH-ACYL-ACP -> TRANS-D2-ENOYL-ACP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
