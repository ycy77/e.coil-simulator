---
entity_id: "gene.b0027"
entity_type: "gene"
name: "lspA"
source_database: "NCBI RefSeq"
source_id: "gene-b0027"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0027"
  - "lspA"
---

# lspA

`gene.b0027`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0027`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lspA (gene.b0027) is a gene entity. It encodes lspA (protein.P00804). Encoded protein function: FUNCTION: This protein specifically catalyzes the removal of signal peptides from prolipoproteins. {ECO:0000255|HAMAP-Rule:MF_00161, ECO:0000269|PubMed:6368552, ECO:0000269|PubMed:6374664, ECO:0000269|PubMed:6378662}. EcoCyc product frame: EG10548-MONOMER. EcoCyc synonyms: lsp. Genomic coordinates: 25207-25701. EcoCyc protein note: lspA encodes prolipoprotein signal peptidase (signal peptidase II) - an inner membrane endopeptidase that cleaves the signal peptide from glyceride modified prolipoproteins including EG10544-MONOMER . Signal peptidase II requires a glyceride modified cysteine residue at the cleavage site . The peptidic antibiotic, globomycin specifically inhibits signal peptidase II activity resulting in the accumulation of glyceride modified prolipoprotein in the inner membrane and cell death . LspA has four predicted membrane-spanning hydrophobic segments . LspA does not have an apparent signal peptide . LspA contains four transmembrane domains and both termini are located in the cytoplasm . lspA is part of a five gene operon (ribF-ileS-lspA-fkpB-ispH) . Reviews:

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03060` Protein export (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00804|protein.P00804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lspA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=lspA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000096,ECOCYC:EG10548,GeneID:944800`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:25207-25701:+; feature_type=gene
