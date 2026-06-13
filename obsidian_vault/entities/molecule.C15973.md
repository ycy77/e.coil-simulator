---
entity_id: "molecule.C15973"
entity_type: "small_molecule"
name: "Enzyme N6-(dihydrolipoyl)lysine"
source_database: "KEGG"
source_id: "C15973"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Enzyme N6-(dihydrolipoyl)lysine"
  - "Dihydrolipoamide-E"
  - "[E2 protein]-N6-[(R)-dihydrolipoyl]-L-lysine"
  - "[Lipoyl-carrier protein E2]-N6-[(R)-dihydrolipoyl]-L-lysine"
---

# Enzyme N6-(dihydrolipoyl)lysine

`molecule.C15973`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15973`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Enzyme N6-(dihydrolipoyl)lysine; Dihydrolipoamide-E; [E2 protein]-N6-[(R)-dihydrolipoyl]-L-lysine; [Lipoyl-carrier protein E2]-N6-[(R)-dihydrolipoyl]-L-lysine EcoCyc common name: a [pyruvate dehydrogenase E2 protein] N6-dihydrolipoyl-L-lysine.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Enzyme N6-(dihydrolipoyl)lysine; Dihydrolipoamide-E; [E2 protein]-N6-[(R)-dihydrolipoyl]-L-lysine; [Lipoyl-carrier protein E2]-N6-[(R)-dihydrolipoyl]-L-lysine

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R12603|reaction.R12603]] `KEGG` `database` - C15973 + C15498 <=> C15972 + C00001 + C01335
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1132|reaction.ecocyc.RXN0-1132]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1133|reaction.ecocyc.RXN0-1133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15973`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
