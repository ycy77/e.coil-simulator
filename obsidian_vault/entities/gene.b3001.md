---
entity_id: "gene.b3001"
entity_type: "gene"
name: "gpr"
source_database: "NCBI RefSeq"
source_id: "gene-b3001"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3001"
  - "gpr"
---

# gpr

`gene.b3001`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3001`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpr (gene.b3001) is a gene entity. It encodes gpr (protein.Q46851). Encoded protein function: FUNCTION: Aldo-keto reductase that catalyzes the stereospecific, NADPH-dependent reduction of L-glyceraldehyde 3-phosphate (L-GAP) to L-glycerol 3-phosphate (L-G3P) (PubMed:18620424). The physiological role of Gpr is the detoxification of L-GAP, which may be formed via non-enzymatic and/or enzymatic racemization of D-GAP (PubMed:18620424). Also contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:12583903, PubMed:16077126). However, the catalytic efficiency of methylglyoxal reductase activity is more than 2 orders of magnitude lower than the L-GAP reductase activity (PubMed:18620424). In addition, exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde and benzaldehyde, D,L-glyceraldehyde, phenylglyoxal, isatin and the model substrate 4-nitrobenzaldehyde (PubMed:12583903, PubMed:16077126). {ECO:0000269|PubMed:12583903, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:18620424, ECO:0000269|PubMed:23990306}. EcoCyc product frame: G7558-MONOMER. EcoCyc synonyms: mgrA, yghZ. Genomic coordinates: 3147897-3148937...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46851|protein.Q46851]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009848,ECOCYC:G7558,GeneID:947480`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3147897-3148937:+; feature_type=gene
