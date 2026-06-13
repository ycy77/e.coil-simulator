---
entity_id: "gene.b2070"
entity_type: "gene"
name: "yegI"
source_database: "NCBI RefSeq"
source_id: "gene-b2070"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2070"
  - "yegI"
---

# yegI

`gene.b2070`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2070`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegI (gene.b2070) is a gene entity. It encodes yegI (protein.P76393). Encoded protein function: FUNCTION: Probable serine/threonine kinase. {ECO:0000269|PubMed:29967116}. EcoCyc product frame: G7109-MONOMER. Genomic coordinates: 2149039-2150985. EcoCyc protein note: YegI, characterized from E. coli B REL606 (YegIEcB) is an inner membrane, eukaryotic-like, serine/threonine kinase . Purified, His-tagged YegIEcB autophosphorylates, primarily on serine residues; kinase activity requires a divalent cation with a preference for Mn2+ and is inhibited by staurosporine; autophosphorylation may be important for YegI activation . Both the protein sequence and the genome context differs between the otherwise closely related K-12 and B strains of E. coli. The YegI protein sequences are 96% identical. While the E. coli B REL606 genome encodes YegI immediatedly downstream of G7111-MONOMER PphC, in E. coli K-12 the two ORFs are separated by the divergently transcribed G7110 yegJ which may disrupt coordinated expression. It is notable that mutations in yegI have been found repeatedly in long-term evolution experiments performed with E. coli B REL606. The E. coli B REL606 PphC dephosphorylates autophosphorylated YegI. The physiological role of the YegI/PphC kinase/phosphatase pair is so far unknown .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76393|protein.P76393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006858,ECOCYC:G7109,GeneID:947159`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2149039-2150985:-; feature_type=gene
