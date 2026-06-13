---
entity_id: "gene.b0809"
entity_type: "gene"
name: "glnQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0809"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0809"
  - "glnQ"
---

# glnQ

`gene.b0809`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0809`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnQ (gene.b0809) is a gene entity. It encodes glnQ (protein.P10346). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for glutamine. Probably responsible for energy coupling to the transport system. EcoCyc product frame: GLNQ-MONOMER. Genomic coordinates: 845741-846463. EcoCyc protein note: GlnQ is the predicted ATP binding subunit of an L-glutamine ABC transporter complex; GlnQ contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by lrp (protein.P0ACJ0), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10346|protein.P10346]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnQ; function=-+
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnQ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002764,ECOCYC:EG10389,GeneID:945435`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:845741-846463:-; feature_type=gene
