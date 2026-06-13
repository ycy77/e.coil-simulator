---
entity_id: "gene.b3463"
entity_type: "gene"
name: "ftsE"
source_database: "NCBI RefSeq"
source_id: "gene-b3463"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3463"
  - "ftsE"
---

# ftsE

`gene.b3463`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3463`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsE (gene.b3463) is a gene entity. It encodes ftsE (protein.P0A9R7). Encoded protein function: FUNCTION: Part of the ABC transporter FtsEX involved in cellular division. Important for assembly or stability of the septal ring. {ECO:0000269|PubMed:14729705}. EcoCyc product frame: FTSE-MONOMER. Genomic coordinates: 3602079-3602747. EcoCyc protein note: FtsE dimerizes and associates with the inner membrane via interaction with FtsX, an integral membrane protein . FtsE and FtsX localize to the cell division site; localization is dependent on FtsZ, FtsA and ZipA, but not on FtsK, FtsQ, FtsL(W) nor FtsI; FtsEX is important for assembly or stability of the septal ring under low-salt growth conditions and under low osmolarity conditions . Depletion of FtsEX does not affect the abundance of FtsK, FtsQ, FtsI nor FtsN in the cytoplasmic membrane . The ATP-binding site mutant, FtsE(D162A) localizes to the septal ring and supports septal ring assembly but impairs septal ring constriction; FtsE may use ATP to promote septal ring constriction . FtsE requires FtsZ for localization to the septal ring . ftsE is non-essential when grown at high salt concentration (>0.5% NaCl); inactivation of ftsE (ftsE::kan) results in a filamented cellular morphology . ftsE and ftsX are located in an operon with ftsY - the latter encoding the SRP receptor...

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9R7|protein.P0A9R7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011313,ECOCYC:EG10340,GeneID:947968`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3602079-3602747:-; feature_type=gene
