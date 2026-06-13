---
entity_id: "molecule.C00157"
entity_type: "small_molecule"
name: "Phosphatidylcholine"
source_database: "KEGG"
source_id: "C00157"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidylcholine"
  - "Lecithin"
  - "Phosphatidyl-N-trimethylethanolamine"
  - "1,2-Diacyl-sn-glycero-3-phosphocholine"
  - "Choline phosphatide"
  - "3-sn-Phosphatidylcholine"
---

# Phosphatidylcholine

`molecule.C00157`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00157`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidylcholine; Lecithin; Phosphatidyl-N-trimethylethanolamine; 1,2-Diacyl-sn-glycero-3-phosphocholine; Choline phosphatide; 3-sn-Phosphatidylcholine EcoCyc common name: a phosphatidylcholine. PHOSPHATIDYLCHOLINE "A phosphatidylcholine" is Phosphoglycerides composed of a GLYCEROL backbone esterified to PHOSPHORYL-CHOLINE and two Fatty-Acids "fatty acids". Phosphatidylcholine is a major component of eukaryotic cell membranes, in which it accounts for 40-60% of total phospholipids. It is also found in an estimated 1015% of bacterial taxa, and especially in bacterial symbionts and pathogens of eukaryotes. Phosphatidylcholine is often referred to by the name lecithin, obtained from ancient Greek for egg yolk (lekithos), from which it was originally isolated. There are two variations of the molecular structure, since either an end carbon or a middle carbon of the glycerol can be attached to the phosphocholine. We have illustrated only one here.

## Biological Role

Consumed as substrate in 6 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidylcholine; Lecithin; Phosphatidyl-N-trimethylethanolamine; 1,2-Diacyl-sn-glycero-3-phosphocholine; Choline phosphatide; 3-sn-Phosphatidylcholine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (6)

- `is_substrate_of` --> [[reaction.R01309|reaction.R01309]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_substrate_of` --> [[reaction.R01313|reaction.R01313]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00060
- `is_substrate_of` --> [[reaction.R01314|reaction.R01314]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00060
- `is_substrate_of` --> [[reaction.R01315|reaction.R01315]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_substrate_of` --> [[reaction.R01316|reaction.R01316]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_substrate_of` --> [[reaction.R01317|reaction.R01317]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00157`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
