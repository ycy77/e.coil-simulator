---
entity_id: "gene.b1581"
entity_type: "gene"
name: "rspA"
source_database: "NCBI RefSeq"
source_id: "gene-b1581"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1581"
  - "rspA"
---

# rspA

`gene.b1581`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1581`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rspA (gene.b1581) is a gene entity. It encodes rspA (protein.P38104). Encoded protein function: FUNCTION: Probably involved in the degradation of homoserine lactone (HSL) or of a metabolite of HSL that signals starvation. EcoCyc product frame: G6839-MONOMER. Genomic coordinates: 1653927-1655141. EcoCyc protein note: The RspA protein may be a bifunctional dehydratase that utilizes both D-mannonate and D-altronate as substrates . However, the enzyme from E. coli CFT037 shows only low catalytic activity with D-mannonate in vitro . Overexpression of RspA prevents homoserine lactone-dependent synthesis of the stationary phase-specific sigma factor σS . Overexpression of HsrA relieves RspA-mediated suppression of σS levels . RspA is similar to Spa2 of Streptomyces ambofaciens and mandelate racemase and chloromuconate cycloisomerase from Pseudomonas putida . RspA: "regulatory in stationary phase"

## Biological Role

Repressed by rspR (protein.P0ACM2). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38104|protein.P38104]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rspA; function=+
- `represses` <-- [[protein.P0ACM2|protein.P0ACM2]] `RegulonDB` `S` - regulator=YdfH; target=rspA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005275,ECOCYC:G6839,GeneID:946126`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1653927-1655141:-; feature_type=gene
