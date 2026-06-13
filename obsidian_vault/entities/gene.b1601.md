---
entity_id: "gene.b1601"
entity_type: "gene"
name: "tqsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1601"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1601"
  - "tqsA"
---

# tqsA

`gene.b1601`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1601`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tqsA (gene.b1601) is a gene entity. It encodes tqsA (protein.P0AFS5). Encoded protein function: FUNCTION: Involved in the transport of the quorum-sensing signal autoinducer 2 (AI-2) (PubMed:16385049). Controls the transport of AI-2 either by enhancing its secretion or inhibiting its uptake and consequently represses biofilm formation and motility and affects the global gene expression in biofilms (PubMed:16385049). {ECO:0000269|PubMed:16385049}. EcoCyc product frame: G6859-MONOMER. EcoCyc synonyms: ydgG. Genomic coordinates: 1673913-1674947. EcoCyc protein note: TqsA has been implicated in autoinducer 2 (AI-2) transport - it may be involved in exporting AI-2 or inhibiting its uptake. A tqsA knockout mutant (K-12 BW25113 ΔtqsA::kan) has significantly less extracellular AI-2 activity and signficantly more intracellular AI-2 activity compared to the wild-type strain, and is more resistant than wild-type to a number of drugs. The tqsA knockout increases biofilm formation in M9 glucose media - a phenotype that is complemented by the expression of tqsA in trans . The protein product is predicted to be a mostly α-helical membrane protein with seven or eight transmembrane segments . TqsA is a member of the Autoinducer-2 Exporter (AI-2E) Family of transporters . tqsA: transporter of quorum-sensing signal AI-2 Review:

## Biological Role

Activated by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFS5|protein.P0AFS5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=tqsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005350,ECOCYC:G6859,GeneID:946142`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1673913-1674947:+; feature_type=gene
