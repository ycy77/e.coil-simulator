---
entity_id: "gene.b1008"
entity_type: "gene"
name: "rutE"
source_database: "NCBI RefSeq"
source_id: "gene-b1008"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1008"
  - "rutE"
---

# rutE

`gene.b1008`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1008`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutE (gene.b1008) is a gene entity. It encodes rutE (protein.P75894). Encoded protein function: FUNCTION: May reduce toxic product malonic semialdehyde to 3-hydroxypropionic acid, which is excreted. RutE is apparently supplemented by YdfG. Required in vivo, but not in vitro in pyrimidine nitrogen degradation. {ECO:0000269|PubMed:16540542}. EcoCyc product frame: G6519-MONOMER. EcoCyc synonyms: ycdI. Genomic coordinates: 1070365-1070955. EcoCyc protein note: E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutE is not required for the release of ammonium from uracil in vitro; it may function as a malonic semialdehyde reductase . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutE insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutE: "pyrimidine utilization E" Reviews:

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75894|protein.P75894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutE; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutE; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003407,ECOCYC:G6519,GeneID:946591`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1070365-1070955:-; feature_type=gene
