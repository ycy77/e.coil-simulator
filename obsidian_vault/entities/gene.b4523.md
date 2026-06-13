---
entity_id: "gene.b4523"
entity_type: "gene"
name: "yciX"
source_database: "NCBI RefSeq"
source_id: "gene-b4523"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4523"
  - "yciX"
---

# yciX

`gene.b4523`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4523`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciX (gene.b4523) is a gene entity. It encodes yciX (protein.P58094). Encoded protein function: Uncharacterized protein YciX EcoCyc product frame: MONOMER0-2886. EcoCyc synonyms: yciX_2. Genomic coordinates: 1335291-1335458. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 8, 2017.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P58094|protein.P58094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yciX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285044,ECOCYC:G0-10513,GeneID:1450257`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1335291-1335458:+; feature_type=gene
