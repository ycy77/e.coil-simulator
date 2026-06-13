---
entity_id: "gene.b0956"
entity_type: "gene"
name: "matP"
source_database: "NCBI RefSeq"
source_id: "gene-b0956"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0956"
  - "matP"
---

# matP

`gene.b0956`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0956`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

matP (gene.b0956) is a gene entity. It encodes matP (protein.P0A8N0). Encoded protein function: FUNCTION: Required for spatial organization of the terminus region of the chromosome (Ter macrodomain) during the cell cycle. Prevents early segregation of duplicated Ter macrodomains during cell division. Binds specifically to matS, which is a 13 bp signature motif repeated within the Ter macrodomain. {ECO:0000255|HAMAP-Rule:MF_01073, ECO:0000269|PubMed:18984159}. EcoCyc product frame: EG12855-MONOMER. EcoCyc synonyms: ycbG. Genomic coordinates: 1018485-1018937. EcoCyc protein note: The MatP protein colocalizes with the chromosomal terminus region in a discrete focus in the cell. MatP binds specifically to matS sites within the Ter macrodomain (MD) both in vitro and in vivo, preventing early segregation of that domain during cell division . Segregation of the dif region depends on MatP and G6464-MONOMER FtsK . After cell division, the Ter MD migrates from the cell pole to mid-cell, where it is anchored via the interaction of MatP with the Z ring-associated protein CPLX0-7686 ZapB . MatP interacts with the CPLX0-2561 complex and displaces it from ter . A contact map of the E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8N0|protein.P0A8N0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003238,ECOCYC:EG12855,GeneID:945570`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1018485-1018937:+; feature_type=gene
