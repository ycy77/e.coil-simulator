---
entity_id: "gene.b0341"
entity_type: "gene"
name: "cynX"
source_database: "NCBI RefSeq"
source_id: "gene-b0341"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0341"
  - "cynX"
---

# cynX

`gene.b0341`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0341`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cynX (gene.b0341) is a gene entity. It encodes cynX (protein.P17583). Encoded protein function: FUNCTION: This protein is part of an active transport system that transports exogenous cyanate into E.coli cells. EcoCyc product frame: CYNX-MONOMER. Genomic coordinates: 359992-361146. EcoCyc protein note: CynX is a putative cyanate transporter. CynX is a member of the major facilitator superfamily (MFS) of transporters , and the cynX gene has been shown to be part of a cyanate-induced operon with cynS and cynT, encoding cyanase and carbonic anhydrase, respectively . However, no phenotype has been observed for a knockout mutation in cynX . Overexpression of cynX confers resistance to bromoacetate .

## Biological Role

Activated by rpoD (protein.P00579), cynR (protein.P27111).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17583|protein.P17583]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cynX; function=+
- `activates` <-- [[protein.P27111|protein.P27111]] `RegulonDB` `S` - regulator=CynR; target=cynX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001175,ECOCYC:EG10177,GeneID:946770`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:359992-361146:+; feature_type=gene
