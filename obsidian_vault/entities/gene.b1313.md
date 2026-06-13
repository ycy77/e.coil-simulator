---
entity_id: "gene.b1313"
entity_type: "gene"
name: "ycjQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1313"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1313"
  - "ycjQ"
---

# ycjQ

`gene.b1313`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1313`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjQ (gene.b1313) is a gene entity. It encodes ycjQ (protein.P76043). Encoded protein function: FUNCTION: Catalyzes the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-gulosides leading to 3-dehydro-D-gulosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Is also able to catalyze the reverse reactions, i.e. the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-gulosides leading to D-gulosides. In vitro, can oxidize D-gulose and methyl beta-D-guloside, and reduce methyl alpha-3-dehydro-D-guloside and methyl beta-3-dehydro-D-guloside. However, the actual specific physiological substrates for this metabolic pathway are unknown. {ECO:0000269|PubMed:30742415}. EcoCyc product frame: G6651-MONOMER. Genomic coordinates: 1374963-1376015. EcoCyc protein note: Purified YcjQ has NAD+-dependent D-guloside dehydrogenase activity .

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76043|protein.P76043]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004412,ECOCYC:G6651,GeneID:945971`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1374963-1376015:+; feature_type=gene
