---
entity_id: "gene.b2347"
entity_type: "gene"
name: "yfdC"
source_database: "NCBI RefSeq"
source_id: "gene-b2347"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2347"
  - "yfdC"
---

# yfdC

`gene.b2347`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2347`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdC (gene.b2347) is a gene entity. It encodes yfdC (protein.P37327). Encoded protein function: Inner membrane protein YfdC EcoCyc product frame: G7217-MONOMER. Genomic coordinates: 2465301-2466233. EcoCyc protein note: YfdC is predicted to be an inner membrane protein with six transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . In the Transporter Classification Database YfdC is an uncharacterised member of the Formate-Nitrite Transporter (FNT) family. YfdC belongs to the YfdC-α subgroup within prokaryotic FNT proteins; molecular modeling suggests that YfdC is not an anion channel but may be selective for neutral or cationic substrates . A variety of potential substrates were identified using an untargeted metabolomics approach .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37327|protein.P37327]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yfdC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007751,ECOCYC:G7217,GeneID:944801`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2465301-2466233:+; feature_type=gene
