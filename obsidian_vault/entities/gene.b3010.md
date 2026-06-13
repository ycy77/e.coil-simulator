---
entity_id: "gene.b3010"
entity_type: "gene"
name: "yqhC"
source_database: "NCBI RefSeq"
source_id: "gene-b3010"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3010"
  - "yqhC"
---

# yqhC

`gene.b3010`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3010`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqhC (gene.b3010) is a gene entity. It encodes yqhC (protein.Q46855). Encoded protein function: FUNCTION: Transcriptional regulator that positively regulates the expression of the yqhD-dkgA operon (PubMed:20543070, PubMed:20676725, PubMed:34248896). Acts by binding directly to the promoter region of yqhD (PubMed:20543070). {ECO:0000269|PubMed:20543070, ECO:0000269|PubMed:20676725, ECO:0000269|PubMed:34248896}. EcoCyc product frame: G7563-MONOMER. Genomic coordinates: 3154262-3155218. EcoCyc protein note: The YqhC transcriptional activator directly binds to the promoter region of the yqhD gene, which contains the SoxS-like binding sequence as well as a 24-bp palindrome . YqhC also regulates dkgA expression . The yqhD and dkgA genes encode NADPH-dependent oxidoreductases, and both are involved in furfural reduction . YqhC belongs to the AraC/XylS transcriptional activator family, as it shows 13.6% amino acid identity with AraC . The identity of the intracellular signal for YqhC is yet to be discovered . Closely related bacteria contain yqhC, yqhD, and dkgA orthologs in the same arrangement as in Escherichia coli LY180. On the other hand, orthologs of yqhC are also present in more distantly related Gram-negative bacteria . It is probable that YqhC regulates its own expression, since it is inducible by furfural...

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46855|protein.Q46855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yqhC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009884,ECOCYC:G7563,GeneID:947491`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3154262-3155218:-; feature_type=gene
