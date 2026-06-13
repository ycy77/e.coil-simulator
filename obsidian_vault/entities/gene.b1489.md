---
entity_id: "gene.b1489"
entity_type: "gene"
name: "dosP"
source_database: "NCBI RefSeq"
source_id: "gene-b1489"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1489"
  - "dosP"
---

# dosP

`gene.b1489`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1489`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dosP (gene.b1489) is a gene entity. It encodes dosP (protein.P76129). Encoded protein function: FUNCTION: Heme-based oxygen sensor protein displaying phosphodiesterase (PDE) activity toward c-di-GMP in response to oxygen availability. Involved in the modulation of intracellular c-di-GMP levels, in association with DosC which catalyzes the biosynthesis of c-di-GMP (diguanylate cyclase activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Has very poor PDE activity on cAMP (PubMed:15995192) but is not active with cGMP, bis(p-nitrophenyl) phosphate or p-nitrophenyl phosphate (PubMed:11970957). Via its PDE activity on c-di-GMP, DosP regulates biofilm formation through the repression of transcription of the csgBAC operon, which encodes curli structural subunits. {ECO:0000269|PubMed:11970957, ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:20553324}. EcoCyc product frame: G6783-MONOMER. EcoCyc synonyms: yddU, dos, pdeO. Genomic coordinates: 1563334-1565733.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76129|protein.P76129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004963,ECOCYC:G6783,GeneID:945815`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1563334-1565733:-; feature_type=gene
