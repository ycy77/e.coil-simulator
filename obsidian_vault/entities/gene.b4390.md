---
entity_id: "gene.b4390"
entity_type: "gene"
name: "nadR"
source_database: "NCBI RefSeq"
source_id: "gene-b4390"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4390"
  - "nadR"
---

# nadR

`gene.b4390`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4390`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadR (gene.b4390) is a gene entity. It encodes nadR (protein.P27278). Encoded protein function: FUNCTION: This enzyme has three activities: DNA binding, nicotinamide mononucleotide (NMN) adenylyltransferase and ribosylnicotinamide (RN) kinase. The DNA-binding domain binds to the nadB operator sequence in an NAD- and ATP-dependent manner. As NAD levels increase within the cell, the affinity of NadR for the nadB operator regions of nadA, nadB, and pncB increases, repressing the transcription of these genes. The RN kinase activity catalyzes the phosphorylation of RN to form nicotinamide ribonucleotide. The NMN adenylyltransferase activity catalyzes the transfer of the AMP moiety of ATP to nicotinamide ribonucleotide to form NAD(+). The NMN adenylyltransferase domain also functions as the NAD and ATP sensor. {ECO:0000269|PubMed:10464228}. EcoCyc product frame: PD04413. EcoCyc synonyms: nadI. Genomic coordinates: 4627315-4628547.

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27278|protein.P27278]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014397,ECOCYC:EG11335,GeneID:948911`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4627315-4628547:+; feature_type=gene
