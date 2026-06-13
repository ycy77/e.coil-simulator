---
entity_id: "complex.ecocyc.CPLX0-8292"
entity_type: "complex"
name: "5-keto-D-gluconate 5-reductase"
source_database: "EcoCyc"
source_id: "CPLX0-8292"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-keto-D-gluconate 5-reductase

`complex.ecocyc.CPLX0-8292`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8292`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9P9|protein.P0A9P9]]

## Enriched Summary

5-Keto-D-gluconate 5-reductase catalyzes the reversible reduction of 5-ketogluconate to D-gluconate. This is the second reaction of the L-idonate catabolic pathway after uptake of L-idonate into the cell. The enzyme specifically reduces 5-ketogluconate using either NADH or NADPH. D-gluconate oxidation by the enzyme can only proceed with NAD as the coenzyme; NADP only results in low specific activity . Based on sequence similarity, IdnO was predicted to be an acetoin dehydrogenase (diacetyl reductase) . Expression of the idnDOTR operon is catabolite repressed and induced by L-idonate or 5-ketogluconate . IdnO: "idonate" Review: 5-Keto-D-gluconate 5-reductase catalyzes the reversible reduction of 5-ketogluconate to D-gluconate. This is the second reaction of the L-idonate catabolic pathway after uptake of L-idonate into the cell. The enzyme specifically reduces 5-ketogluconate using either NADH or NADPH. D-gluconate oxidation by the enzyme can only proceed with NAD as the coenzyme; NADP only results in low specific activity . Based on sequence similarity, IdnO was predicted to be an acetoin dehydrogenase (diacetyl reductase) . Expression of the idnDOTR operon is catabolite repressed and induced by L-idonate or 5-ketogluconate . IdnO: "idonate" Review:

## Biological Role

Catalyzes GLUCONATE-5-DEHYDROGENASE-RXN (reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN), RXN0-7101 (reaction.ecocyc.RXN0-7101).

## Annotation

5-Keto-D-gluconate 5-reductase catalyzes the reversible reduction of 5-ketogluconate to D-gluconate. This is the second reaction of the L-idonate catabolic pathway after uptake of L-idonate into the cell. The enzyme specifically reduces 5-ketogluconate using either NADH or NADPH. D-gluconate oxidation by the enzyme can only proceed with NAD as the coenzyme; NADP only results in low specific activity . Based on sequence similarity, IdnO was predicted to be an acetoin dehydrogenase (diacetyl reductase) . Expression of the idnDOTR operon is catabolite repressed and induced by L-idonate or 5-ketogluconate . IdnO: "idonate" Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7101|reaction.ecocyc.RXN0-7101]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9P9|protein.P0A9P9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8292`
- `QSPROTEOME:QS00196527`

## Notes

2*protein.P0A9P9
