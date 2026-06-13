---
entity_id: "gene.b3617"
entity_type: "gene"
name: "kbl"
source_database: "NCBI RefSeq"
source_id: "gene-b3617"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3617"
  - "kbl"
---

# kbl

`gene.b3617`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3617`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kbl (gene.b3617) is a gene entity. It encodes kbl (protein.P0AB77). Encoded protein function: FUNCTION: Catalyzes the cleavage of 2-amino-3-ketobutyrate to glycine and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00985, ECO:0000269|PubMed:2104756}. EcoCyc product frame: AKBLIG-MONOMER. Genomic coordinates: 3791355-3792551.

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB77|protein.P0AB77]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kbl; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=kbl; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=kbl; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=kbl; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011832,ECOCYC:EG10512,GeneID:948138`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3791355-3792551:-; feature_type=gene
