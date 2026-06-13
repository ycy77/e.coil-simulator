---
entity_id: "gene.b0509"
entity_type: "gene"
name: "glxR"
source_database: "NCBI RefSeq"
source_id: "gene-b0509"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0509"
  - "glxR"
---

# glxR

`gene.b0509`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0509`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glxR (gene.b0509) is a gene entity. It encodes glxR (protein.P77161). Encoded protein function: 2-hydroxy-3-oxopropionate reductase (EC 1.1.1.60) (Tartronate semialdehyde reductase) (TSAR) EcoCyc product frame: G6278-MONOMER. EcoCyc synonyms: glxB1, ybbQ. Genomic coordinates: 536586-537464. EcoCyc protein note: Tartronate semialdehyde reductase 2 (GlxR) catalyzes the reversible reactions of NAD+-dependent oxidation of D-glycerate and the NADH-dependent reduction of tartronate semialdehyde . Expression of tartronate semialdehyde reductase is induced by anaerobic growth with allantoin as the sole source of nitrogen and is induced more than 100-fold by growth on glyoxylate as the sole source of carbon . A glxR mutant lacks the ability to utilize glyoxylate . Review:

## Biological Role

Repressed by allR (protein.P0ACN4).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77161|protein.P77161]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=glxR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001759,ECOCYC:G6278,GeneID:945146`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:536586-537464:+; feature_type=gene
