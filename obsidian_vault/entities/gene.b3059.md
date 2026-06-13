---
entity_id: "gene.b3059"
entity_type: "gene"
name: "plsY"
source_database: "NCBI RefSeq"
source_id: "gene-b3059"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3059"
  - "plsY"
---

# plsY

`gene.b3059`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3059`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plsY (gene.b3059) is a gene entity. It encodes plsY (protein.P60782). Encoded protein function: FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can also utilize acyl-CoA as fatty acyl donor, but not acyl-PO(4) (Probable). {ECO:0000305|PubMed:17645809}. EcoCyc product frame: EG11674-MONOMER. EcoCyc synonyms: ygiH. Genomic coordinates: 3204694-3205311. EcoCyc protein note: PlsY, together with EG11437-MONOMER PlsX, can substitute for GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) in synthesis of 2-Acyl-sn-glycerol-3-phosphates required for initiation of phospholipid synthesis and fine-tune the levels of other lipids involved in the structure of the cell envelope . Most Gram-negative proteobacteria have both the PlsX/PlsY and PlsB systems . PlsY is an inner membrane protein with five predicted transmembrane domains. The C terminus is located in the cytoplasm . PlsY is similar to the Bacillus subtilis and Streptococcus pneumoniae PlsY proteins, which function as the glycerol-3-phosphate acyltransferase for phospholipid biosynthesis, a function that is filled by PlsB in E. coli. However, a plsX plsY double deletion is lethal . Yoshimura et al. hypothesize that PlsX and PlsY play a role in regulating the intracellular concentration of acyl-ACP...

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60782|protein.P60782]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010042,ECOCYC:EG11674,GeneID:947561`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3204694-3205311:+; feature_type=gene
