---
entity_id: "gene.b0898"
entity_type: "gene"
name: "ycaD"
source_database: "NCBI RefSeq"
source_id: "gene-b0898"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0898"
  - "ycaD"
---

# ycaD

`gene.b0898`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0898`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaD (gene.b0898) is a gene entity. It encodes ycaD (protein.P21503). Encoded protein function: Uncharacterized MFS-type transporter YcaD EcoCyc product frame: YCAD-MONOMER. Genomic coordinates: 945871-947019. EcoCyc protein note: The YcaD protein is an uncharacterised member of the Drug:H+ Antiporter-4 (DHA4) family within the Major Facilitator Superfamily (MFS) of transporters .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21503|protein.P21503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ycaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003056,ECOCYC:EG11242,GeneID:945515`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:945871-947019:+; feature_type=gene
