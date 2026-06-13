---
entity_id: "gene.b2830"
entity_type: "gene"
name: "rppH"
source_database: "NCBI RefSeq"
source_id: "gene-b2830"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2830"
  - "rppH"
---

# rppH

`gene.b2830`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2830`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rppH (gene.b2830) is a gene entity. It encodes rppH (protein.P0A776). Encoded protein function: FUNCTION: Master regulator of 5'-end-dependent mRNA decay (PubMed:18202662). Accelerates the degradation of transcripts by removing pyrophosphate from the 5'-end of triphosphorylated RNA, leading to a more labile monophosphorylated state that can stimulate subsequent ribonuclease cleavage (PubMed:18202662). Preferentially hydrolyzes diadenosine penta-phosphate with ATP as one of the reaction products (PubMed:11479323). Also able to hydrolyze diadenosine hexa- and tetra-phosphate (PubMed:11479323). Has no activity on diadenosine tri-phosphate, ADP-ribose, NADH and UDP-glucose (PubMed:11479323). In an RNase PH (rph) wild-type strain background, RppH is not required for maturation of tRNAs; however, strains with the truncated rph allele (for example K12 W1485 and its derivatives MG1655 and W3110) require RppH for maturation of certain monocistronic tRNAs with short (<5 nucleotides) leader sequences (PubMed:28808133). In the meningitis causing strain E.coli K1, has been shown to play a role in HBMEC (human brain microvascular endothelial cells) invasion in vitro (PubMed:10760174). {ECO:0000269|PubMed:10760174, ECO:0000269|PubMed:11479323, ECO:0000269|PubMed:18202662, ECO:0000269|PubMed:28808133}. EcoCyc product frame: G7459-MONOMER. EcoCyc synonyms: ygdP, nudH...

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A776|protein.P0A776]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009276,ECOCYC:G7459,GeneID:947300`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2968447-2968977:-; feature_type=gene
