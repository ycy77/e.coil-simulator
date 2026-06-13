---
entity_id: "gene.b3764"
entity_type: "gene"
name: "maoP"
source_database: "NCBI RefSeq"
source_id: "gene-b3764"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3764"
  - "maoP"
---

# maoP

`gene.b3764`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3764`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

maoP (gene.b3764) is a gene entity. It encodes maoP (protein.P0ADN2). Encoded protein function: FUNCTION: Involved in the organization of the Ori region of the chromosome into a macrodomain (MD) (PubMed:27627105). It constrains DNA mobility in the Ori macrodomain and limits long-distance DNA interactions with other chromosomal regions (PubMed:27627105). Is part of a system composed of two elements: MaoP, which can act both in cis and in trans, and a cis-acting target sequence called maoS (PubMed:27627105). {ECO:0000269|PubMed:27627105}. EcoCyc product frame: EG11450-MONOMER. EcoCyc synonyms: yifE. Genomic coordinates: 3948086-3948424. EcoCyc protein note: The MaoP protein and the MAOS maoS site, which is located in the intergenic region upstream of maoP, are involved in the organization of the Ori macrodomain. Together, they constrain the mobility of the Ori macrodomain . MaoP was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . maoP belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . In a large-scale TraDIS screen, loss of maoP appeared to be beneficial for biofilm formation. However, a maoP deletion mutant was deficient in biofilm formation . Expression may be positively regulated by the small RNA RybB...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADN2|protein.P0ADN2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012298,ECOCYC:EG11450,GeneID:948274`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3948086-3948424:+; feature_type=gene
