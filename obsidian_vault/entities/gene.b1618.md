---
entity_id: "gene.b1618"
entity_type: "gene"
name: "uidR"
source_database: "NCBI RefSeq"
source_id: "gene-b1618"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1618"
  - "uidR"
---

# uidR

`gene.b1618`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1618`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uidR (gene.b1618) is a gene entity. It encodes uidR (protein.P0ACT6). Encoded protein function: FUNCTION: Repressor for the uidRABC (gusRABC) operon. EcoCyc product frame: G6867-MONOMER. EcoCyc synonyms: gusR. Genomic coordinates: 1696462-1697052. EcoCyc protein note: The "β-d-glucuronides repressor," UidR, is a transcriptional repressor. UidR negatively regulates its own synthesis and represses transcription of the uid operon, which is involved in transport and degradation of β-glucosides . This regulator is involved in the degradation of sugar acids and is subject to catabolic repression in the presence of glucose and at low levels of cyclic AMP. Although little is known about the regulating mechanism of UidR, it has been shown to act as a repressor, binding to a putative inverted repeat sequence in a cooperative process with UxuR . In 1986, Blanco et al. proposed that total repression of UidR is achieved in the presence of UxuR, suggesting the possibility that UidR and UxuR form a complex. Independently, each repressor binds to DNA separately . In the BL21 strain, UidR (GusR) can be inhibited by the presence of glucuronides, as they can bind to the protein GusR to release the DNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACT6|protein.P0ACT6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005415,ECOCYC:G6867,GeneID:946150`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1696462-1697052:-; feature_type=gene
