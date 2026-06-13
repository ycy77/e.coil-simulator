---
entity_id: "gene.b2422"
entity_type: "gene"
name: "cysA"
source_database: "NCBI RefSeq"
source_id: "gene-b2422"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2422"
  - "cysA"
---

# cysA

`gene.b2422`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2422`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysA (gene.b2422) is a gene entity. It encodes cysA (protein.P16676). Encoded protein function: FUNCTION: Part of the ABC transporter complex CysAWTP involved in sulfate/thiosulfate import. Responsible for energy coupling to the transport system. EcoCyc product frame: CYSA-MONOMER. Genomic coordinates: 2539717-2540814. EcoCyc protein note: cysA encodes the predicted ATP-binding subunit of a high-affinity sulfate/thiosulfate uptake system; CysA contains sequence motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16676|protein.P16676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysA; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007986,ECOCYC:EG10183,GeneID:946889`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2539717-2540814:-; feature_type=gene
