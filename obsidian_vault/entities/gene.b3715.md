---
entity_id: "gene.b3715"
entity_type: "gene"
name: "yieH"
source_database: "NCBI RefSeq"
source_id: "gene-b3715"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3715"
  - "yieH"
---

# yieH

`gene.b3715`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3715`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yieH (gene.b3715) is a gene entity. It encodes yieH (protein.P31467). Encoded protein function: FUNCTION: Catalyzes strongly the dephosphorylation of 6-phosphogluconate (6P-Glu) and slightly the dephosphorylation of dihydroxyacetone phosphate (DHAP) and phosphoenolpyruvate (PEP). Also hydrolyzes both purines (GMP and IMP) and pyrimidines as secondary substrates. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. EcoCyc product frame: EG11725-MONOMER. Genomic coordinates: 3896774-3897439. EcoCyc protein note: YieH is a 6-phosphogluconate phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Purine and pyrimidine nucleotides are secondary substrates . The phosphatase activity of YieH was first discovered in a high-throughput screen of purified proteins .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31467|protein.P31467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yieH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012153,ECOCYC:EG11725,GeneID:948232`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3896774-3897439:+; feature_type=gene
