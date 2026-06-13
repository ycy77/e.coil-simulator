---
entity_id: "gene.b1409"
entity_type: "gene"
name: "ynbB"
source_database: "NCBI RefSeq"
source_id: "gene-b1409"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1409"
  - "ynbB"
---

# ynbB

`gene.b1409`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1409`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynbB (gene.b1409) is a gene entity. It encodes ynbB (protein.P76091). Encoded protein function: FUNCTION: Involved in the biosynthesis of MPIase, a glycolipid essential for membrane protein integration and cell growth (PubMed:30718729, PubMed:30739787, PubMed:30936205). Overproduction of YnbB causes an increase in the MPIase level (PubMed:30718729). Under CdsA-depleted conditions, YnbB overproduction restores MPIase expression, but not phospholipid biosynthesis, suggesting that it can function as a backup for MPIase biosynthesis, but not for phospholipid biosynthesis (PubMed:30718729, PubMed:30739787). {ECO:0000269|PubMed:30718729, ECO:0000269|PubMed:30739787, ECO:0000269|PubMed:30936205}. EcoCyc product frame: G6728-MONOMER. Genomic coordinates: 1478226-1479122. EcoCyc protein note: The C-terminal halves of YnbB and CDPDIGLYSYN-MONOMER (CdsA) have significant sequence homology; YnbB overproduction causes an increase in the level of CPD-15878; YnbB is implicated in the biosynthesis of MPIase . YnbB is predicted to be an inner membrane protein with eight transmembrane domains; experimental topology analysis suggests the C terminus is located in the periplasm . A ynbB deletion mutant is more sensitive to ampicillin than wild type .

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76091|protein.P76091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004706,ECOCYC:G6728,GeneID:945972`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1478226-1479122:+; feature_type=gene
