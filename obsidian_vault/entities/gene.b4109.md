---
entity_id: "gene.b4109"
entity_type: "gene"
name: "rdcA"
source_database: "NCBI RefSeq"
source_id: "gene-b4109"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4109"
  - "rdcA"
---

# rdcA

`gene.b4109`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4109`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rdcA (gene.b4109) is a gene entity. It encodes rdcA (protein.P0DM85). Encoded protein function: FUNCTION: Regulatory protein that, together with its partner protein RdcB, activates the diguanylate cyclase E (DgcE) to control CsgD and biofilm matrix production (PubMed:31022167). Binds GTP and shows GTPase activity (PubMed:23994470, PubMed:31022167). The GTPase activity is essential for activation of DgcE (PubMed:31022167). The GTP-bound form of RdcA might be unable to activate DgcE because GTP may act as an allosteric inhibitor (PubMed:31022167). {ECO:0000269|PubMed:23994470, ECO:0000269|PubMed:31022167}.; FUNCTION: Is also proposed to be involved in chromosome segregation (PubMed:23994470). Is important for the colocalization of sister nascent DNA strands after replication fork passage during DNA replication, and for positioning and subsequent partitioning of sister chromosomes (PubMed:23994470). This activity is not affected by the presence or absence of GTP (PubMed:23994470). {ECO:0000269|PubMed:23994470}. EcoCyc product frame: EG11210-MONOMER. EcoCyc synonyms: yjdA, crfC. Genomic coordinates: 4327135-4329363.

## Biological Role

Repressed by yciT (protein.P76034). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DM85|protein.P0DM85]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76034|protein.P76034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013456,ECOCYC:EG11210,GeneID:948620`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4327135-4329363:+; feature_type=gene
