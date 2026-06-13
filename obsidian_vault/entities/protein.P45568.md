---
entity_id: "protein.P45568"
entity_type: "protein"
name: "dxr"
source_database: "UniProt"
source_id: "P45568"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dxr ispC yaeM b0173 JW0168"
---

# dxr

`protein.P45568`

## Static

- Type: `protein`
- Source: `UniProt:P45568`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). {ECO:0000269|PubMed:10631325, ECO:0000269|PubMed:10787409, ECO:0000269|PubMed:9707569}.

## Biological Role

Component of 1-deoxy-D-xylulose 5-phosphate reductoisomerase (complex.ecocyc.DXPREDISOM-CPLX).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). {ECO:0000269|PubMed:10631325, ECO:0000269|PubMed:10787409, ECO:0000269|PubMed:9707569}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DXPREDISOM-CPLX|complex.ecocyc.DXPREDISOM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0173|gene.b0173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45568`
- `KEGG:ecj:JW0168;eco:b0173;ecoc:C3026_00790;`
- `GeneID:93777252;945019;`
- `GO:GO:0019288; GO:0030145; GO:0030604; GO:0042802; GO:0051484; GO:0070402; GO:1990065`
- `EC:1.1.1.267`

## Notes

1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reductoisomerase) (2-C-methyl-D-erythritol 4-phosphate synthase)
