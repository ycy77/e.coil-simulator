---
entity_id: "molecule.C02463"
entity_type: "small_molecule"
name: "Precorrin 2"
source_database: "KEGG"
source_id: "C02463"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Precorrin 2"
  - "Dihydrosirohydrochlorin"
---

# Precorrin 2

`molecule.C02463`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02463`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Precorrin 2; Dihydrosirohydrochlorin EcoCyc common name: precorrin-2. The intermediates of the pathway between UROPORPHYRINOGEN-III and CPD-9049 are termed precorrin-n, where n refers to the number of methyl groups that have been added to the UROPORPHYRINOGEN-III framework. They include CPD-9038, DIHYDROSIROHYDROCHLORIN, CPD-642, CPD-643, CPD-651, CPD-662, CPD-675, CPD-679, CPD-14845 and CPD-686.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Precorrin 2; Dihydrosirohydrochlorin

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R03194|reaction.R03194]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_product_of` --> [[reaction.ecocyc.RXN-13403|reaction.ecocyc.RXN-13403]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8675|reaction.ecocyc.RXN-8675]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN|reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02463`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
