---
entity_id: "gene.b1524"
entity_type: "gene"
name: "glsB"
source_database: "NCBI RefSeq"
source_id: "gene-b1524"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1524"
  - "glsB"
---

# glsB

`gene.b1524`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1524`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glsB (gene.b1524) is a gene entity. It encodes glsA2 (protein.P0A6W0). Encoded protein function: Glutaminase 2 (EC 3.5.1.2) EcoCyc product frame: G6810-MONOMER. EcoCyc synonyms: yneH. Genomic coordinates: 1612325-1613251. EcoCyc protein note: GlsB (YneH) is a glutaminase that is highly selective for L-glutamine. Based on the pH profile of the enzymatic activity, GlsB was proposed to correspond to the previously identified GLUTAMINB-CPLX of E. coli B. Glutamine binding exhibits positive cooperativity . A glsB deletion mutant grows two times slower than wild-type on glutamine as the sole source of carbon and nitrogen . A ΔglsB mutant has no defect in glutamine-dependent acid resistance . Review:

## Biological Role

Activated by yneJ (protein.P77309).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6W0|protein.P0A6W0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77309|protein.P77309]] `RegulonDB` `S` - regulator=PtrR; target=glsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005086,ECOCYC:G6810,GeneID:944973`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1612325-1613251:-; feature_type=gene
