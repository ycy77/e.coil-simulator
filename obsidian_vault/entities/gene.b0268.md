---
entity_id: "gene.b0268"
entity_type: "gene"
name: "yagE"
source_database: "NCBI RefSeq"
source_id: "gene-b0268"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0268"
  - "yagE"
---

# yagE

`gene.b0268`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0268`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagE (gene.b0268) is a gene entity. It encodes yagE (protein.P75682). Encoded protein function: FUNCTION: Catalyzes the formation of 2-keto-3-deoxy-gluconate (KDG) from pyruvate and glyceraldehyde (PubMed:21294156). May also function as a 2-dehydro-3-deoxy-D-pentonate aldolase (PubMed:23233208). Overexpression leads to increased growth (over 2 hours) in the presence of the antibiotics norfloxacin, ampicillin and streptomycin (PubMed:21294156). {ECO:0000269|PubMed:21294156, ECO:0000305|PubMed:23233208}. EcoCyc product frame: G6140-MONOMER. Genomic coordinates: 282278-283186.

## Biological Role

Repressed by xynR (protein.P77300).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75682|protein.P75682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77300|protein.P77300]] `RegulonDB` `C` - regulator=XynR; target=yagE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000921,ECOCYC:G6140,GeneID:944925`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:282278-283186:+; feature_type=gene
