---
entity_id: "gene.b4481"
entity_type: "gene"
name: "wecF"
source_database: "NCBI RefSeq"
source_id: "gene-b4481"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4481"
  - "wecF"
---

# wecF

`gene.b4481`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4481`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecF (gene.b4481) is a gene entity. It encodes wecF (protein.P56258). Encoded protein function: FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA-Fuc4NAc (Lipid III), the third lipid-linked intermediate involved in ECA synthesis. {ECO:0000269|PubMed:11673418}. EcoCyc product frame: G7800-MONOMER. EcoCyc synonyms: yifM, b4404, rff, rffT, b4405. Genomic coordinates: 3977525-3978604. EcoCyc protein note: The rffT gene encodes Fuc4NAc (4-acetamido-4,6-dideoxy-D-galactose) transferase, which catalyzes the synthesis of lipid III, the final intermediate in the enterobacterial common antigen (ECA) biosynthetic pathway. Lipid III constitutes the trisaccharide repeat unit of ECA, which is utilized for the synthesis of ECA heteropolysaccharide chains. A rffT mutant exhibits a defect in lipid III biosynthesis . A wecF/rffT mutant exhibits several phenotypes that are indirect effects of outer membrane defects due to buildup of ECA-lipid II, including increased transcription from the degP promoter, sensitivity to LamB or to bile salts, and stimulation of SigmaE and Cpx signaling . A wecF/rffT mutant shows a defect in production of a cyclic form of enterobacterial common antigen that is water-soluble and found in wild type cells...

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56258|protein.P56258]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0174115,ECOCYC:G7800,GeneID:2847677`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3977525-3978604:+; feature_type=gene
