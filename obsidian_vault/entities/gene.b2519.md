---
entity_id: "gene.b2519"
entity_type: "gene"
name: "pbpC"
source_database: "NCBI RefSeq"
source_id: "gene-b2519"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2519"
  - "pbpC"
---

# pbpC

`gene.b2519`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2519`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pbpC (gene.b2519) is a gene entity. It encodes pbpC (protein.P76577). Encoded protein function: FUNCTION: Cell wall formation. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a transpeptidase C-terminal domain which may not be functional. {ECO:0000269|PubMed:10542235}. EcoCyc product frame: G7322-MONOMER. EcoCyc synonyms: yfgN. Genomic coordinates: 2645013-2647325. EcoCyc protein note: pbpC encodes a HMW penicillin binding protein (PBP) known as PBP1C. PBP1C (like CPLX0-7717 PBP1A and CPLX0-3951 PBP1B) contains characteristic transglycosylase and transpeptidase amino acid motifs but only transglycosylase activity has been assayed . PBP1C does not bind most of the β-lactams known to bind other PBPs leading to speculation that PBP1C does not have transpeptidase activity (the transpeptidase region is also responsible for penicillin binding) . PPB1C is predicted to contain a single transmembrane domain which anchors the cell to the inner membrane with the remainder of the enzyme located in the periplasm . PBP1C is responsible for 75% of transglycosylase activity in ether pemeabilized cells, but only less than 3% in crude membranes; PBP1C-specific murein synthesizing activity is sensitive to moenomycin . PBP1C binds 35S-labeled penicillin; maximum binding occurs at pH 5 . PBP1C binds moxalactam poorly...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76577|protein.P76577]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008294,ECOCYC:G7322,GeneID:947152`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2645013-2647325:-; feature_type=gene
