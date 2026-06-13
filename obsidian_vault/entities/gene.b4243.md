---
entity_id: "gene.b4243"
entity_type: "gene"
name: "ridA"
source_database: "NCBI RefSeq"
source_id: "gene-b4243"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4243"
  - "ridA"
---

# ridA

`gene.b4243`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4243`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ridA (gene.b4243) is a gene entity. It encodes ridA (protein.P0AF93). Encoded protein function: FUNCTION: Accelerates the release of ammonia from reactive enamine/imine intermediates of the PLP-dependent threonine dehydratase (IlvA) in the low water environment of the cell. It catalyzes the deamination of enamine/imine intermediates to yield 2-ketobutyrate and ammonia. It is required for the detoxification of reactive intermediates of IlvA due to their highly nucleophilic abilities. Involved in the isoleucine biosynthesis. {ECO:0000250|UniProtKB:Q7CP78}. EcoCyc product frame: G7877-MONOMER. EcoCyc synonyms: yjgF. Genomic coordinates: 4470527-4470913.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF93|protein.P0AF93]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ridA; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=ridA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013886,ECOCYC:G7877,GeneID:948771`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4470527-4470913:-; feature_type=gene
