---
entity_id: "gene.b1659"
entity_type: "gene"
name: "punR"
source_database: "NCBI RefSeq"
source_id: "gene-b1659"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1659"
  - "punR"
---

# punR

`gene.b1659`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1659`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

punR (gene.b1659) is a gene entity. It encodes punR (protein.P0ACR2). Encoded protein function: FUNCTION: Transcriptional regulator that activates the expression of punC, which encodes a purine nucleoside transporter (PubMed:34413462). In the presence of adenine, it binds to a conserved 23-bp palindromic motif in the intergenic region between punR and punC (PubMed:34413462). {ECO:0000269|PubMed:34413462}. EcoCyc product frame: EG12140-MONOMER. EcoCyc synonyms: ydhB. Genomic coordinates: 1738866-1739798. EcoCyc protein note: PunR, formerly named YdhB, regulates a gene involved in the purine transport process in the presence of adenosine . This protein belongs to the LysR family of HTH-type transcriptional regulators . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain . PunR appears to recognize and bind to a palindromic DNA binding motif of 23 bp . Genome-wide PunR-binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The punR gene is located in the genome in an inverted position from its target gene . This arrangement in the genome appears to be conserved in other proteobacteria...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACR2|protein.P0ACR2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005547,ECOCYC:EG12140,GeneID:945208`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1738866-1739798:-; feature_type=gene
