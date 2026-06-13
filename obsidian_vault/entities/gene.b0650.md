---
entity_id: "gene.b0650"
entity_type: "gene"
name: "hscC"
source_database: "NCBI RefSeq"
source_id: "gene-b0650"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0650"
  - "hscC"
---

# hscC

`gene.b0650`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0650`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hscC (gene.b0650) is a gene entity. It encodes hscC (protein.P77319). Encoded protein function: FUNCTION: Chaperone that exhibits ATPase activity (PubMed:12054669, PubMed:12183460, PubMed:9735342). It interacts with the RNA polymerase sigma factor RpoD (sigma-70) and inhibits its activity (PubMed:12059959). HscC may function under specific conditions where the transient inhibition of sigma-70 is required (PubMed:12059959). It does not inhibit the activity of sigma-32 (PubMed:12059959). Binds peptides and can prevent aggregation of denatured substrates (PubMed:12183460). However, HscC may not have general chaperone activity as it does not assist refolding of a denatured model substrate (PubMed:12183460). {ECO:0000269|PubMed:12054669, ECO:0000269|PubMed:12059959, ECO:0000269|PubMed:12183460, ECO:0000269|PubMed:9735342}. EcoCyc product frame: G6357-MONOMER. EcoCyc synonyms: ybeW. Genomic coordinates: 681723-683393. EcoCyc protein note: HscC (Hsc62) is an E. coli-specific member of the Hsc66 subfamily of Hsp70-family chaperones . Hsc62 exhibits ATPase activity , but does not show chaperone activity toward a denatured protein substrate . Hsc62 associates with σ70 and negatively regulates σ70 activity . It is the ATPase domain of Hsc62 that is essential for its activity towards σ70...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77319|protein.P77319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002225,ECOCYC:G6357,GeneID:945218`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:681723-683393:-; feature_type=gene
