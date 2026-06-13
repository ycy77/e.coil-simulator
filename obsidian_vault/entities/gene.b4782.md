---
entity_id: "gene.b4782"
entity_type: "gene"
name: "pssL"
source_database: "NCBI RefSeq"
source_id: "gene-b4782"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4782"
  - "pssL"
---

# pssL

`gene.b4782`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4782`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pssL (gene.b4782) is a gene entity. It encodes pssL (protein.P0DSG0). Encoded protein function: FUNCTION: May serve a regulatory role in expression of downstream gene pssA; in a pssL-pssA-lacZ fusion, mutation of the start codon of pssA to a stop codon in pssL decreases expression of beta-galactosidase, suggesting translation of the 2 genes is coupled. {ECO:0000269|PubMed:30837344}. EcoCyc product frame: MONOMER0-4494. Genomic coordinates: 2722702-2722743. EcoCyc protein note: PssL was identified as a previously unannotated small protein. Introduction of a stop codon into the pssL ORF leads to 30% decreased expression of the downstream gene, pssA, in a lacZ fusion construct, suggesting translational coupling .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSG0|protein.P0DSG0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pssL; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17028,GeneID:63925645`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2722702-2722743:+; feature_type=gene
