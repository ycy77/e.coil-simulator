---
entity_id: "gene.b2835"
entity_type: "gene"
name: "lplT"
source_database: "NCBI RefSeq"
source_id: "gene-b2835"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2835"
  - "lplT"
---

# lplT

`gene.b2835`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2835`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lplT (gene.b2835) is a gene entity. It encodes lplT (protein.P39196). Encoded protein function: FUNCTION: Catalyzes the facilitated diffusion of 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) into the cell. {ECO:0000269|PubMed:15661733}. EcoCyc product frame: EG12455-MONOMER. EcoCyc synonyms: ygeD. Genomic coordinates: 2972669-2973862. EcoCyc protein note: LplT is a phospholipid flippase that catalyses the facilitated diffusion of lysophospholipid across the inner membrane bilayer. LplT functions to reutilize 2-acylglycerophosphoethanolamine (2-acyl-GPE) that is generated in the periplasm during the maturation of the major outer membrane lipoprotein (Lpp); LplT import provides substrate for the AAS-MONOMER "Aas" catalysed 2-acyl-GPE acyltransferase reaction . lplT forms an operon with aas . LplT interacts directly with Aas; LplT and Aas form a functional complex in vivo which facilitates specific and efficient reacylation of lysophospholipids . LplT/Aas function plays a role in the resistance of gram-negative bacteria to mammalian secretory phospholipase A2 (sPLA2) . In a ΔfadD background, loss of lplT results in significant accumulation of acyl-GPE . E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39196|protein.P39196]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009300,ECOCYC:EG12455,GeneID:947317`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2972669-2973862:-; feature_type=gene
