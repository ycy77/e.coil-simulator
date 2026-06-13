---
entity_id: "protein.P37678"
entity_type: "protein"
name: "sgbH"
source_database: "UniProt"
source_id: "P37678"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgbH yiaQ b3581 JW3553"
---

# sgbH

`protein.P37678`

## Static

- Type: `protein`
- Source: `UniProt:P37678`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871}. YiaQ/SgbH is one of two known 3-keto-L-gulonate-6-phosphate decarboxylases in E. coli . Expression from the yiaK promoter is moderately induced by fucose and ascorbate , and increased amounts of YiaQ protein are detected after aerobic growth on ascorbate . The presence of the amino acids proline, threonine, glutamate, glutamine or aspartate in the medium is required for yiaK promoter activity. Cells that overexpress the yiaK operon due to a mutation in the YiaJ repressor gain the ability to utilize L-ascorbate as the sole source of carbon . Review:

## Biological Role

Catalyzes RXN0-705 (reaction.ecocyc.RXN0-705).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-705|reaction.ecocyc.RXN0-705]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3581|gene.b3581]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37678`
- `KEGG:ecj:JW3553;eco:b3581;ecoc:C3026_19415;`
- `GeneID:948098;`
- `GO:GO:0004590; GO:0006207; GO:0016052; GO:0019854; GO:0033982; GO:0046872`
- `EC:4.1.1.85`

## Notes

3-keto-L-gulonate-6-phosphate decarboxylase SgbH (KGPDC) (EC 4.1.1.85) (3-dehydro-L-gulonate-6-phosphate decarboxylase)
