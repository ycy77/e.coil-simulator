---
entity_id: "gene.b0810"
entity_type: "gene"
name: "glnP"
source_database: "NCBI RefSeq"
source_id: "gene-b0810"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0810"
  - "glnP"
---

# glnP

`gene.b0810`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0810`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnP (gene.b0810) is a gene entity. It encodes glnP (protein.P0AEQ6). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for glutamine; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: GLNP-MONOMER. Genomic coordinates: 846460-847119. EcoCyc protein note: GlnP is the predicted integral membrane subunit of an L-glutamine ABC transport sytem

## Biological Role

Repressed by glnZ (gene.b4836), glnG (protein.P0AFB8). Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEQ6|protein.P0AEQ6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnP; function=-+
- `represses` <-- [[gene.b4836|gene.b4836]] `RegulonDB` `S` - regulator=GlnZ; target=glnP; function=-
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnP; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002766,ECOCYC:EG10388,GeneID:945621`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:846460-847119:-; feature_type=gene
