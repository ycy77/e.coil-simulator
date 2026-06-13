---
entity_id: "gene.b1315"
entity_type: "gene"
name: "ycjS"
source_database: "NCBI RefSeq"
source_id: "gene-b1315"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1315"
  - "ycjS"
---

# ycjS

`gene.b1315`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1315`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjS (gene.b1315) is a gene entity. It encodes ycjS (protein.P77503). Encoded protein function: FUNCTION: Catalyzes the NADH-dependent reduction of the oxo group at C3 of 3-dehydro-D-glucosides leading to D-glucosides. Probably functions in a metabolic pathway that transforms D-gulosides to D-glucosides. Can use 3-dehydro-D-glucose, methyl alpha-3-dehydro-D-glucoside and methyl beta-3-dehydro-D-glucoside as substrates in vitro. However, the actual specific physiological substrates for this metabolic pathway are unknown. To a lesser extent, is also able to catalyze the reverse reactions, i.e. the NAD(+)-dependent oxidation of the hydroxyl group at C3 of D-glucosides leading to 3-dehydro-D-glucosides. Cannot act on UDP-glucose, UDP-N-acetyl-D-glucosamine, D-glucosamine, N-acetyl-D-glucosamine, or UDP-D-galactose. {ECO:0000269|PubMed:30742415}. EcoCyc product frame: G6653-MONOMER. Genomic coordinates: 1376832-1377887. EcoCyc protein note: Purified YcjS has NAD+-dependent D-glucoside 3-dehydrogenase activity . YcjS was predicted to be an NAD+-dependent dehydrogenase . Based on sequence similarity, YcjS was also predicted to be a D-galactose 1-dehydrogenase . However, this is not consistent with the known biochemistry of E. coli, which metabolizes galactose via the PWY-6317 "Leloir pathway".

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77503|protein.P77503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004416,ECOCYC:G6653,GeneID:948589`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1376832-1377887:+; feature_type=gene
