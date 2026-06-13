---
entity_id: "gene.b3271"
entity_type: "gene"
name: "yhdZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3271"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3271"
  - "yhdZ"
---

# yhdZ

`gene.b3271`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3271`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdZ (gene.b3271) is a gene entity. It encodes yhdZ (protein.P45769). Encoded protein function: FUNCTION: Probably part of a binding-protein-dependent transport system YdhWXYZ for an amino acid. Probably responsible for energy coupling to the transport system. EcoCyc product frame: YHDZ-MONOMER. Genomic coordinates: 3422436-3423194. EcoCyc protein note: YhdZ is predicted to be the ATP-binding subunit of a putative ABC transporter; YhdZ contains sequence motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45769|protein.P45769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=yhdZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010738,ECOCYC:EG12837,GeneID:947763`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3422436-3423194:+; feature_type=gene
