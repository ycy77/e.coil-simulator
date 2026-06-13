---
entity_id: "gene.b3191"
entity_type: "gene"
name: "mlaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3191"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3191"
  - "mlaB"
---

# mlaB

`gene.b3191`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3191`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaB (gene.b3191) is a gene entity. It encodes mlaB (protein.P64602). Encoded protein function: FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaB plays critical roles in both the assembly and activity of the complex. May act by modulating MlaF structure and stability (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. EcoCyc product frame: G7658-MONOMER. EcoCyc synonyms: yrbB. Genomic coordinates: 3336963-3337256. EcoCyc protein note: mlaB encodes a cytoplasmic subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaB is implicated in a retrograde phospholipid trafficking pathway; MlaB is a predicted cytoplasmic protein with a STAS domain . MlaB forms a stable complex with MlaF, MlaE and MlaD; MlaB is required for the stability and/or assembly of the complex; an MlaFEB complex containing an MlaB variant with a mutation in the STAS domain (MlaBT52A) has no intrinsic ATPase activity in vitro...

## Biological Role

Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64602|protein.P64602]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=mlaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010487,ECOCYC:G7658,GeneID:947954`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3336963-3337256:-; feature_type=gene
