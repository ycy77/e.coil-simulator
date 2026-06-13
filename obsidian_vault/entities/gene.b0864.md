---
entity_id: "gene.b0864"
entity_type: "gene"
name: "artP"
source_database: "NCBI RefSeq"
source_id: "gene-b0864"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0864"
  - "artP"
---

# artP

`gene.b0864`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0864`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

artP (gene.b0864) is a gene entity. It encodes artP (protein.P0AAF6). Encoded protein function: FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:8801422}. EcoCyc product frame: ARTP-MONOMER. Genomic coordinates: 903006-903734. EcoCyc protein note: ArtP is predicted to be the ATP-binding subunit of an L- arginine ABC transporter. Sequence analysis indicates that ArtP is highly homologous to the HisP ATP-binding protein of the histine/LAO (lysine/arginine/ornithine) ABC transporter system in Salmonella typhimurium. artP contains a conserved ATP-binding consensus site .

## Biological Role

Repressed by argR (protein.P0A6D0), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAF6|protein.P0AAF6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=artP; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=artP; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=artP; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002939,ECOCYC:EG11624,GeneID:945489`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:903006-903734:-; feature_type=gene
