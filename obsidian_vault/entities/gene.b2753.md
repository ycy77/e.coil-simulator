---
entity_id: "gene.b2753"
entity_type: "gene"
name: "iap"
source_database: "NCBI RefSeq"
source_id: "gene-b2753"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2753"
  - "iap"
---

# iap

`gene.b2753`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2753`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iap (gene.b2753) is a gene entity. It encodes iap (protein.P10423). Encoded protein function: FUNCTION: This protein, presumably an aminopeptidase, mediates the conversion of E.coli alkaline phosphatase isozyme 1, to isozymes 2 and 3 by removing, one by one, the two N-terminal arginine residues. EcoCyc product frame: EG10488-MONOMER. Genomic coordinates: 2876581-2877618. EcoCyc protein note: Alkaline phosphatase isozyme conversion protein is responsible for the stepwise removal of the two amino-terminal arginines from alkaline phosphatase isozyme 1, creating isozymes 2 and 3 in the process . This is presumably an aminopeptidase activity, as it can be inhibited by protease inhibitors . Alkaline phosphatase isozyme conversion protein has a characteristic signal peptide at its amino-terminus and can be found as both full-length and signal-peptide-cleaved forms in the cell. It is a membrane-associated protein that acts in the periplasm . Efficieny of secretion of alkaline phosphatase isozyme conversion protein is reduced when phosphatidylethanolamine is depleted, resulting in less effective modification of alkaline phosphatase .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10423|protein.P10423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009033,ECOCYC:EG10488,GeneID:947215`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2876581-2877618:+; feature_type=gene
