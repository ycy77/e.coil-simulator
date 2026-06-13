---
entity_id: "protein.P0AG82"
entity_type: "protein"
name: "pstS"
source_database: "UniProt"
source_id: "P0AG82"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pstS phoS b3728 JW3706"
---

# pstS

`protein.P0AG82`

## Static

- Type: `protein`
- Source: `UniProt:P0AG82`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import. PstS is the periplasmic, phosphate binding protein of the ATP dependent, high affinity phosphate transport sytem in E. coli K-12. PstS consists of two globular domains separated by a deep cleft which forms the phosphate binding site . PstS binds monobasic (H2PO4-) and dibasic (H2PO42-) phosphates but discriminates against sulphate . The aspartate residue at position 81 forms a short (low barrier) hydrogen bond with phosphate . PstS can discriminate phosphate from arsenate up to an 800 fold molar excess of arsenate . A pstS D81N mutant has no effect on phosphate binding but disturbs the discrimination against arsenate approximately 10-fold and the discrimination against sulfate about 100-fold . pstS insertion mutants were identified in a screen for genes that are important for surviving exposure to ionizing radiation (IR). A pstS deletion mutant has a substantial decrease in survival upon exposure to increasing doses of IR . It was determined by Genomic SELEX screening that the upstream region of the gene pstS is a target of the transcriptional factor CusR .

## Biological Role

Component of phosphate ABC transporter (complex.ecocyc.ABC-27-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-27-CPLX|complex.ecocyc.ABC-27-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3728|gene.b3728]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG82`
- `KEGG:ecj:JW3706;eco:b3728;ecoc:C3026_20205;`
- `GeneID:75205442;948237;`
- `GO:GO:0006817; GO:0006974; GO:0009314; GO:0016020; GO:0030288; GO:0035435; GO:0042301; GO:0055052`

## Notes

Phosphate-binding protein PstS (PBP)
