---
entity_id: "gene.b0638"
entity_type: "gene"
name: "cobC"
source_database: "NCBI RefSeq"
source_id: "gene-b0638"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0638"
  - "cobC"
---

# cobC

`gene.b0638`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0638`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cobC (gene.b0638) is a gene entity. It encodes cobC (protein.P52086). Encoded protein function: FUNCTION: Catalyzes the conversion of adenosylcobalamin 5'-phosphate to adenosylcobalamin (vitamin B12); involved in the assembly of the nucleotide loop of cobalamin. Also catalyzes the hydrolysis of the phospho group from alpha-ribazole 5'-phosphate to form alpha-ribazole. {ECO:0000250|UniProtKB:P39701}. EcoCyc product frame: RIBAZOLEPHOSPHAT-MONOMER. EcoCyc synonyms: phpB. Genomic coordinates: 669296-669907. EcoCyc protein note: The CobC protein has not been characterised in E. coli K-12 but is predicted to be an adenosylcobalamin 5'-phosphate phosphatase by homology with cobC from Salmonella typhimurium. Early studies in S. typhimurium suggested that CobC was an α-ribazole phosphatase but more recently it was shown that adenosylcobalamin 5'-phosphate was the preferred substrate and that CobC catalyses the last step of adenosylcobalamin (coenzyme B12) biosynthesis .

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52086|protein.P52086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002185,ECOCYC:G6349,GeneID:945246`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:669296-669907:-; feature_type=gene
