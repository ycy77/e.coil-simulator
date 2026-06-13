---
entity_id: "gene.b3973"
entity_type: "gene"
name: "birA"
source_database: "NCBI RefSeq"
source_id: "gene-b3973"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3973"
  - "birA"
---

# birA

`gene.b3973`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3973`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

birA (gene.b3973) is a gene entity. It encodes birA (protein.P06709). Encoded protein function: FUNCTION: Acts both as a biotin--[acetyl-CoA-carboxylase] ligase and a biotin-operon repressor. In the presence of ATP, BirA activates biotin to form the BirA-biotinyl-5'-adenylate (BirA-bio-5'-AMP or holoBirA) complex. HoloBirA can either transfer the biotinyl moiety to the biotin carboxyl carrier protein (BCCP) subunit of acetyl-CoA carboxylase, or bind to the biotin operator site and inhibit transcription of the operon. {ECO:0000255|HAMAP-Rule:MF_00978, ECO:0000269|PubMed:12527300, ECO:0000269|PubMed:2667763, ECO:0000269|PubMed:6129246, ECO:0000269|PubMed:8003500}. EcoCyc product frame: BIOTINLIG-MONOMER. EcoCyc synonyms: bioR, dhbB. Genomic coordinates: 4173082-4174047. EcoCyc protein note: BirA is a bifunctional protein that exhibits biotin ligase activity and also acts as the DNA binding transcriptional repressor of the biotin operon . The effector of BirA transcriptional repression activity, biotinyl-5'-adenylate (bio-5'-AMP), is also a substrate in the BirA-mediated biotinylation of the biotin carboxyl carrier protein monomer (apoBCCP), and this relationship results in repression of the biotin operon when the abundance of apoBCCP (and therefore the cellular demand for biotin) is reduced...

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06709|protein.P06709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013001,ECOCYC:EG10123,GeneID:948469`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4173082-4174047:+; feature_type=gene
