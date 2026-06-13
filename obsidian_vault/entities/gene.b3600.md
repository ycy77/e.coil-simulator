---
entity_id: "gene.b3600"
entity_type: "gene"
name: "mtlD"
source_database: "NCBI RefSeq"
source_id: "gene-b3600"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3600"
  - "mtlD"
---

# mtlD

`gene.b3600`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3600`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtlD (gene.b3600) is a gene entity. It encodes mtlD (protein.P09424). Encoded protein function: Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17) EcoCyc product frame: MANNPDEHYDROG-MONOMER. Genomic coordinates: 3774424-3775572. EcoCyc protein note: Mannitol is the most common natural hexitol and can serve as a carbon source for E. coli. After entering the cell via a dedicated PTS transporter, mannitol-1-phosphate 5-dehydrogenase (MtlD) oxidizes mannitol-1-phosphate to fructose-6-phosphate in a reversible reaction . MtlD activity is induced by growth on mannitol. An mtlD mutant does not grow on mannitol as the sole carbon source . MtlD: "mannitol"

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09424|protein.P09424]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mtlD; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=mtlD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011767,ECOCYC:EG10616,GeneID:948117`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3774424-3775572:+; feature_type=gene
