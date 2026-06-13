---
entity_id: "gene.b0401"
entity_type: "gene"
name: "brnQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0401"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0401"
  - "brnQ"
---

# brnQ

`gene.b0401`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0401`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

brnQ (gene.b0401) is a gene entity. It encodes brnQ (protein.P0AD99). Encoded protein function: FUNCTION: Liv-II branched chain amino acid transport system, which transports leucine, valine and isoleucine (PubMed:4590465, PubMed:4945181). Also acts as a low-affinity threonine transporter (PubMed:37025642). This activity has probably minor relevance for normal cellular physiology, but BrnQ may form the main entry point when the threonine concentration in the external environment reaches a toxic level (PubMed:37025642). {ECO:0000269|PubMed:37025642, ECO:0000269|PubMed:4590465, ECO:0000269|PubMed:4945181}. EcoCyc product frame: BRNQ-MONOMER. EcoCyc synonyms: hrbA. Genomic coordinates: 419591-420910. EcoCyc protein note: BrnQ is a probable branched chain amino acid transporter. BrnQ is highly similar to the Salmonella typhimurium BrnQ branched chain amino acid transporter and very probably corresponds to the LIV-II branched chain amino acid transport system in E. coli, which has been shown to transport leucine, valine, and isoleucine . In the Transporter Classification Database BrnQ is a member of the LIVCS family of branched chain amino acid transporters and probably functions as a branched chain amino acid:Na+ symporter. BrnQ is a low-affinity threonine transporter that is of minor relevance for normal cell physiology .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD99|protein.P0AD99]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=brnQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001394,ECOCYC:EG12168,GeneID:945042`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:419591-420910:+; feature_type=gene
