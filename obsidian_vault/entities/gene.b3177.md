---
entity_id: "gene.b3177"
entity_type: "gene"
name: "folP"
source_database: "NCBI RefSeq"
source_id: "gene-b3177"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3177"
  - "folP"
---

# folP

`gene.b3177`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3177`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folP (gene.b3177) is a gene entity. It encodes folP (protein.P0AC13). Encoded protein function: FUNCTION: Catalyzes the condensation of para-aminobenzoate (pABA) with 6-hydroxymethyl-7,8-dihydropterin diphosphate (DHPt-PP) to form 7,8-dihydropteroate (H2Pte), the immediate precursor of folate derivatives. {ECO:0000269|PubMed:368012, ECO:0000269|PubMed:37419898}. EcoCyc product frame: H2PTEROATESYNTH-MONOMER. EcoCyc synonyms: dhpS. Genomic coordinates: 3324063-3324911.

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC13|protein.P0AC13]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010441,ECOCYC:EG50011,GeneID:947691`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3324063-3324911:-; feature_type=gene
