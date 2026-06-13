---
entity_id: "gene.b1491"
entity_type: "gene"
name: "digH"
source_database: "NCBI RefSeq"
source_id: "gene-b1491"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1491"
  - "digH"
---

# digH

`gene.b1491`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1491`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

digH (gene.b1491) is a gene entity. It encodes digH (protein.P64426). Encoded protein function: FUNCTION: Divisome-localized glycosyl hydrolase that cleaves peptide-free (denuded) peptidoglycans. Has either glucosaminidase or muramidase activity. {ECO:0000269|PubMed:32152098}. EcoCyc product frame: G6785-MONOMER. EcoCyc synonyms: yddW. Genomic coordinates: 1567504-1568823. EcoCyc protein note: DigH is a a-denuded-peptidoglycan denuded glycan specific hydrolase with either glucosaminidase or muramidase activity . DigH-mediated hydrolysis of denuded glycans contributes to peptidoglycan degradation at the division septum . DigH contains a single glycosyl hydrolase-like 10 (GHL10) domain and a predicted lipoprotein signal sequence; the protein localizes to the outer membrane. In a reaction containing the N-acetylmuramyl-L-alanine amidase G6452-MONOMER "AmiD", purified, soluble DigH cleaves peptidoglycan sacculi to produce a large fraction of disaccharides containing N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) without a 1,6-anhydro linkage, and a small fraction of GlcNAc-1,6-anhydroMurNAc; no cleavage is observed in the absence of AmiD . Overexpression of digH suppresses the growth and division defect of a Δtol-pal mutant (in LB lacking NaCL at 42°C); suppressed cells continue to produce outer membrane vesicles when grown in minimal medium...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64426|protein.P64426]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004970,ECOCYC:G6785,GeneID:945975`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1567504-1568823:-; feature_type=gene
