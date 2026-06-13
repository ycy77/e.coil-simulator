---
entity_id: "molecule.C01242"
entity_type: "small_molecule"
name: "[Protein]-S8-aminomethyldihydrolipoyllysine"
source_database: "KEGG"
source_id: "C01242"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "[Protein]-S8-aminomethyldihydrolipoyllysine"
  - "[H-protein]-S-aminomethyldihydrolipoyllysine"
  - "S-Aminomethyldihydrolipoylprotein"
  - "[Glycine-cleavage complex H protein]-S-aminomethyl-N6-dihydrolipoyl-L-lysine"
  - "[GCSH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine"
  - "[GcvH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine"
---

# [Protein]-S8-aminomethyldihydrolipoyllysine

`molecule.C01242`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01242`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: [Protein]-S8-aminomethyldihydrolipoyllysine; [H-protein]-S-aminomethyldihydrolipoyllysine; S-Aminomethyldihydrolipoylprotein; [Glycine-cleavage complex H protein]-S-aminomethyl-N6-dihydrolipoyl-L-lysine; [GCSH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine; [GcvH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: [Protein]-S8-aminomethyldihydrolipoyllysine; [H-protein]-S-aminomethyldihydrolipoyllysine; S-Aminomethyldihydrolipoylprotein; [Glycine-cleavage complex H protein]-S-aminomethyl-N6-dihydrolipoyl-L-lysine; [GCSH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine; [GcvH]-S-aminomethyl-N6-dihydrolipoyl-L-lysine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R03425|reaction.R03425]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011
- `is_substrate_of` --> [[reaction.R04125|reaction.R04125]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01242`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
