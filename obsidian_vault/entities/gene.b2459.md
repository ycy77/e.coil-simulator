---
entity_id: "gene.b2459"
entity_type: "gene"
name: "eutT"
source_database: "NCBI RefSeq"
source_id: "gene-b2459"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2459"
  - "eutT"
---

# eutT

`gene.b2459`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2459`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutT (gene.b2459) is a gene entity. It encodes eutT (protein.P65643). Encoded protein function: FUNCTION: Converts cyanocobalamin (CN-B12) to adenosylcobalamin (AdoCbl), the inducer of the eut operon. Is not active on cobinamide nor other intermediates in the adenosylcobalamin synthetic pathway. Allows full induction of the eut operon. {ECO:0000250|UniProtKB:Q9ZFV4}. EcoCyc product frame: G7289-MONOMER. EcoCyc synonyms: ypfB. Genomic coordinates: 2573502-2574305. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 7, 2018.

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P65643|protein.P65643]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008100,ECOCYC:G7289,GeneID:946939`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2573502-2574305:-; feature_type=gene
