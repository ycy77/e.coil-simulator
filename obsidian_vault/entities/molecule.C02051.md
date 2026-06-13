---
entity_id: "molecule.C02051"
entity_type: "small_molecule"
name: "Lipoylprotein"
source_database: "KEGG"
source_id: "C02051"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lipoylprotein"
  - "[H-protein]-lipoyllysine"
  - "[GCSH]-N6-lipoyl-L-lysine"
  - "[GcvH]-N6-lipoyl-L-lysine"
  - "[Glycine cleavage system H]-N6-lipoyl-L-lysine"
  - "[Glycine-cleavage complex H protein]-N6-lipoyl-L-lysine"
---

# Lipoylprotein

`molecule.C02051`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02051`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lipoylprotein; [H-protein]-lipoyllysine; [GCSH]-N6-lipoyl-L-lysine; [GcvH]-N6-lipoyl-L-lysine; [Glycine cleavage system H]-N6-lipoyl-L-lysine; [Glycine-cleavage complex H protein]-N6-lipoyl-L-lysine EcoCyc common name: lipoamide.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Lipoylprotein; [H-protein]-lipoyllysine; [GCSH]-N6-lipoyl-L-lysine; [GcvH]-N6-lipoyl-L-lysine; [Glycine cleavage system H]-N6-lipoyl-L-lysine; [Glycine-cleavage complex H protein]-N6-lipoyl-L-lysine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R03425|reaction.R03425]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.PYRUVATEDECARB-RXN|reaction.ecocyc.PYRUVATEDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02051`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
