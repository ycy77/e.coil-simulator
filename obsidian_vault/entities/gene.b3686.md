---
entity_id: "gene.b3686"
entity_type: "gene"
name: "ibpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3686"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3686"
  - "ibpB"
---

# ibpB

`gene.b3686`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3686`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibpB (gene.b3686) is a gene entity. It encodes ibpB (protein.P0C058). Encoded protein function: FUNCTION: Associates with aggregated proteins, together with IbpA, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954, ECO:0000269|PubMed:9556585}. EcoCyc product frame: EG11535-MONOMER. EcoCyc synonyms: hslS, htpE. Genomic coordinates: 3866469-3866897.

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C058|protein.P0C058]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ibpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012054,ECOCYC:EG11535,GeneID:948192`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3866469-3866897:-; feature_type=gene
