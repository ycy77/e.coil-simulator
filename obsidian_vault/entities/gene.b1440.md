---
entity_id: "gene.b1440"
entity_type: "gene"
name: "ydcS"
source_database: "NCBI RefSeq"
source_id: "gene-b1440"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1440"
  - "ydcS"
---

# ydcS

`gene.b1440`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1440`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcS (gene.b1440) is a gene entity. It encodes ydcS (protein.P76108). Encoded protein function: FUNCTION: Catalyzes the formation of short polymers of R-3-hydroxybutyrate (cPHB) (PubMed:18640095). Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. During natural transformation, may bind dsDNA and convey it to the inner membrane channel formed by YdcV (Probable). {ECO:0000269|PubMed:18640095, ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}. EcoCyc product frame: YDCS-MONOMER. Genomic coordinates: 1511654-1512799. EcoCyc protein note: The periplasmic protein,YdcS is a predicted to be the binding protein of an uncharacterized ABC transporter . YdcS is implicated in double strand (ds) DNA transport across the inner membrane during natural and chemical transformation; a ydcS deletion mutant has significantly decreased rates of natural and chemical transformation compared to wild type . Purified YdcS has poly-3-hydroxybutyrate (PHB) synthase activity; a ydcS deletion mutant contains approximately 30% less PHB complexed to proteins (cPHB) in the outer membrane compared to wild type; the addition of PHB to outer membrane proteins in the periplasm may facilitate their insertion into the outer membrane (see also )...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76108|protein.P76108]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydcS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004803,ECOCYC:G6751,GeneID:946005`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1511654-1512799:+; feature_type=gene
