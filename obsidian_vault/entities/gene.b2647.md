---
entity_id: "gene.b2647"
entity_type: "gene"
name: "ypjA"
source_database: "NCBI RefSeq"
source_id: "gene-b2647"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2647"
  - "ypjA"
---

# ypjA

`gene.b2647`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2647`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ypjA (gene.b2647) is a gene entity. It encodes ypjA (protein.P52143). Encoded protein function: FUNCTION: Upon overexpression shows increased adherence to polyvinyl chloride (PVC) plates, increased mature biofilm formation (PubMed:15659678). {ECO:0000269|PubMed:15659678}. EcoCyc product frame: G7382-MONOMER. Genomic coordinates: 2778146-2782726. EcoCyc protein note: YpjA was identified as a protein with similarity to antigen 43 (Ag43), a self-recognizing surface adhesin. Deletion of the ypjA gene has no significant effect on adhesion, while increased expression of YpjA causes an increase in adhesion to solid surfaces. Neither deleting nor overexpressing ypjA appears to affect on biofilm formation . An E. coli DH5α ypjA::Tn5 mutant produces significantly less outer membrane vesicles than the wild type .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52143|protein.P52143]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ypjA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008713,ECOCYC:G7382,GeneID:948630`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2778146-2782726:-; feature_type=gene
