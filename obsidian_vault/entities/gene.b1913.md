---
entity_id: "gene.b1913"
entity_type: "gene"
name: "uvrC"
source_database: "NCBI RefSeq"
source_id: "gene-b1913"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1913"
  - "uvrC"
---

# uvrC

`gene.b1913`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1913`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uvrC (gene.b1913) is a gene entity. It encodes uvrC (protein.P0A8G0). Encoded protein function: FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrC both incises the 5' and 3' sides of the lesion. The N-terminal half is responsible for the 3' incision and the C-terminal half is responsible for the 5' incision. {ECO:0000269|PubMed:10671556, ECO:0000269|PubMed:1387639}. EcoCyc product frame: EG11063-MONOMER. Genomic coordinates: 1992874-1994706.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8G0|protein.P0A8G0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uvrC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006370,ECOCYC:EG11063,GeneID:947203`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1992874-1994706:-; feature_type=gene
