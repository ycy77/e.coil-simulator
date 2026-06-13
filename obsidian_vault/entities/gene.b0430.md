---
entity_id: "gene.b0430"
entity_type: "gene"
name: "cyoC"
source_database: "NCBI RefSeq"
source_id: "gene-b0430"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0430"
  - "cyoC"
---

# cyoC

`gene.b0430`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0430`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyoC (gene.b0430) is a gene entity. It encodes cyoC (protein.P0ABJ3). Encoded protein function: FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. EcoCyc product frame: CYOC-MONOMER. Genomic coordinates: 448046-448660. EcoCyc protein note: CyoC is subunit III of the 4 subunit cytochrome bo complex. Subunit III is required for expression of a functional enzyme . The CyoC polypeptide contains five transmembrane helices .

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABJ3|protein.P0ABJ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyoC; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=cyoC; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=cyoC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001491,ECOCYC:EG10180,GeneID:946897`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:448046-448660:-; feature_type=gene
