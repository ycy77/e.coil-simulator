---
entity_id: "gene.b2667"
entity_type: "gene"
name: "ygaV"
source_database: "NCBI RefSeq"
source_id: "gene-b2667"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2667"
  - "ygaV"
---

# ygaV

`gene.b2667`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2667`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygaV (gene.b2667) is a gene entity. It encodes ygaV (protein.P77295). Encoded protein function: FUNCTION: Transcriptional regulator that regulates large-scale gene expression in response to sulfide (PubMed:40005711). May act as a global regulator responsible for redox homeostasis (PubMed:40005711). It functions as both a repressor and an activator (PubMed:36552568, PubMed:40005711). In the absence of sulfide compounds, it negatively regulates many anaerobic respiratory genes, including formate, fumarate, lactate, nitrate and nitrite reductase genes (PubMed:36552568). In the presence of hydrogen sulfide (H(2)S), YgaV activity is attenuated, leading to the expression of anaerobic respiratory and ROS scavenging genes, which contributes to redox homeostasis, reactive oxygen species (ROS) scavenging and antibiotic tolerance (PubMed:36552568). It responds to H(2)O(2) scavenging and increases antibiotic tolerance under H(2)S-atmospheric conditions (PubMed:36552568). It also negatively regulates its own expression by binding to the ygaVP promoter region (PubMed:18245262, PubMed:36552568). May also be involved in regulatory mechanisms that operate independently of sulfide (PubMed:40005711). {ECO:0000269|PubMed:18245262, ECO:0000269|PubMed:36552568, ECO:0000269|PubMed:40005711}. EcoCyc product frame: G7397-MONOMER. Genomic coordinates: 2797211-2797510...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77295|protein.P77295]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygaV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008784,ECOCYC:G7397,GeneID:947136`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2797211-2797510:+; feature_type=gene
