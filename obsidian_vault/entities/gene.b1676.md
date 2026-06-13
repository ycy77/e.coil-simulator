---
entity_id: "gene.b1676"
entity_type: "gene"
name: "pykF"
source_database: "NCBI RefSeq"
source_id: "gene-b1676"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1676"
  - "pykF"
---

# pykF

`gene.b1676`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1676`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pykF (gene.b1676) is a gene entity. It encodes pykF (protein.P0AD61). Encoded protein function: FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305|PubMed:8591049}. EcoCyc product frame: PKI-MONOMER. Genomic coordinates: 1755698-1757110.

## Biological Role

Repressed by cra (protein.P0ACP1).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD61|protein.P0AD61]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=pykF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005600,ECOCYC:EG10804,GeneID:946179`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1755698-1757110:+; feature_type=gene
