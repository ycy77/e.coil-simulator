---
entity_id: "protein.P27833"
entity_type: "protein"
name: "wecE"
source_database: "UniProt"
source_id: "P27833"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecE rffA yifI b3791 JW3765"
---

# wecE

`protein.P27833`

## Static

- Type: `protein`
- Source: `UniProt:P27833`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of dTDP-4-amino-4,6-dideoxy-D-galactose (dTDP-Fuc4N) from dTDP-4-keto-6-deoxy-D-glucose (dTDP-D-Glc4O) and L-glutamate. {ECO:0000255|HAMAP-Rule:MF_02026, ECO:0000269|PubMed:15271350}. dTDP-4-dehydro-6-deoxy-D-glucose transaminase is involved in the biosynthesis of enterobacterial common antigen (ECA). This enzyme catalyzes the conversion of dTDP-4-keto-6-deoxy-D-glucose to dTDP-D-thomosamine . Crystal structures of the enzyme have been solved . While gel filtration showed a molecular weight of 180 kDa, suggesting a homotetrameric structure , the crystal structure showed a homodimeric configuration . The conserved active site Lys181 residue forms the internal aldimine with the PLP cofactor. The stereochemical specificity of the enzyme for amination of the C4 stereocenter, forming the C4-R configuration, is determined by a mode of nucleotide binding (a "base flip" mechanism) that differs from that of other C4 sugar aminotransferases and results in reorientation of the sugar moiety . wecE mutants do not produce ECA and accumulate the pathway intermediate C55-PP-GLCNAC-MANNACA ECA-lipid II, leading to a sensitivity to bile salts and triggering cell envelope stress responses . A wecE mutation was also identified in a screen for mutations that cause altered cell shapes...

## Biological Role

Catalyzes dTDP-4-amino-4,6-dideoxy-D-galactose:2-oxoglutarate aminotransferase (reaction.R04438). Component of dTDP-4-dehydro-6-deoxy-D-glucose transaminase (complex.ecocyc.CPLX0-7990).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of dTDP-4-amino-4,6-dideoxy-D-galactose (dTDP-Fuc4N) from dTDP-4-keto-6-deoxy-D-glucose (dTDP-D-Glc4O) and L-glutamate. {ECO:0000255|HAMAP-Rule:MF_02026, ECO:0000269|PubMed:15271350}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04438|reaction.R04438]] `KEGG` `database` - via EC:2.6.1.59
- `is_component_of` --> [[complex.ecocyc.CPLX0-7990|complex.ecocyc.CPLX0-7990]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3791|gene.b3791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27833`
- `KEGG:ecj:JW3765;eco:b3791;ecoc:C3026_20525;`
- `GeneID:948296;`
- `GO:GO:0000271; GO:0009246; GO:0019180; GO:0030170; GO:0042802`
- `EC:2.6.1.59`

## Notes

dTDP-4-amino-4,6-dideoxygalactose transaminase (EC 2.6.1.59)
