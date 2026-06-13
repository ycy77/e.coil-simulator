---
entity_id: "gene.b0571"
entity_type: "gene"
name: "cusR"
source_database: "NCBI RefSeq"
source_id: "gene-b0571"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0571"
  - "cusR"
---

# cusR

`gene.b0571`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0571`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusR (gene.b0571) is a gene entity. It encodes cusR (protein.P0ACZ8). Encoded protein function: FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Activates the expression of cusCFBA, hiuH and plasmid pRJ1004 gene pcoE in response to increasing levels of copper or silver ions. Can also increase the basal-level expression of copper resistance gene operon pcoABCD. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}. EcoCyc product frame: MONOMER0-4180. EcoCyc synonyms: ylcA. Genomic coordinates: 594760-595443. EcoCyc protein note: CusR, "Cu-sensing regulator", regulates genes related to the copper and silver efflux systems under anaerobic growth and under extreme copper stress in aerobic growth . CusR belongs to the two-component system CusS/CusR, which responds to increases in the copper concentration. Both cusR, encoding the response regulator, and cusS, encoding the sensor kinase, are organized in an operon that is located next to and in the opposite direction to an operon whose expression is activated by CusR . CusR is able to bind to the cusRS-cusCFBA intergenic region in both its phosphorylated and unphosphorylated forms, but in its unphosphorylated form it binds to many other targets in the genome...

## Biological Role

Activated by rpoD (protein.P00579), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACZ8|protein.P0ACZ8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusR; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusR; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusR; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001948,ECOCYC:G6319,GeneID:945003`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:594760-595443:-; feature_type=gene
