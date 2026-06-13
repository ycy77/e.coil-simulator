---
entity_id: "protein.P76373"
entity_type: "protein"
name: "ugd"
source_database: "UniProt"
source_id: "P76373"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ugd pmrE udg yefA b2028 JW2010"
---

# ugd

`protein.P76373`

## Static

- Type: `protein`
- Source: `UniProt:P76373`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

UDP-glucose 6-dehydrogenase (UDP-Glc dehydrogenase) (UDP-GlcDH) (UDPGDH) (EC 1.1.1.22)

## Biological Role

Catalyzes UDP-glucose:NAD+ 6-oxidoreductase (reaction.R00286). Component of UDP-glucose 6-dehydrogenase (complex.ecocyc.CPLX0-8098).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

UDP-glucose 6-dehydrogenase (UDP-Glc dehydrogenase) (UDP-GlcDH) (UDPGDH) (EC 1.1.1.22)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00286|reaction.R00286]] `KEGG` `database` - via EC:1.1.1.22
- `is_component_of` --> [[complex.ecocyc.CPLX0-8098|complex.ecocyc.CPLX0-8098]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2028|gene.b2028]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76373`
- `KEGG:ecj:JW2010;eco:b2028;ecoc:C3026_11430;`
- `GeneID:946571;`
- `GO:GO:0003979; GO:0006065; GO:0009103; GO:0009242; GO:0051287`
- `EC:1.1.1.22`

## Notes

UDP-glucose 6-dehydrogenase (UDP-Glc dehydrogenase) (UDP-GlcDH) (UDPGDH) (EC 1.1.1.22)
