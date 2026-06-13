---
entity_id: "reaction.ecocyc.RXN-9655"
entity_type: "reaction"
name: "RXN-9655"
source_database: "EcoCyc"
source_id: "RXN-9655"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9655

`reaction.ecocyc.RXN-9655`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9655`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a specific instance of the β-hydroxydecanoyl-ACP dehydrase reaction. This reaction is part of the elongation of unsaturated fatty acids. EcoCyc reaction equation: Beta-hydroxydecanoyl-ACPs -> Trans-D2-decenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT. This is a specific instance of the β-hydroxydecanoyl-ACP dehydrase reaction. This reaction is part of the elongation of unsaturated fatty acids.

## Biological Role

Catalyzed by β-hydroxyacyl-acyl carrier protein dehydratase/isomerase (complex.ecocyc.FABA-CPLX), 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)
- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Annotation

This is a specific instance of the β-hydroxydecanoyl-ACP dehydrase reaction. This reaction is part of the elongation of unsaturated fatty acids.

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)
- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABA-CPLX|complex.ecocyc.FABA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-9655`

## Notes

Beta-hydroxydecanoyl-ACPs -> Trans-D2-decenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT
