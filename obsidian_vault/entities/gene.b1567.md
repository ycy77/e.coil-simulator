---
entity_id: "gene.b1567"
entity_type: "gene"
name: "ydfW"
source_database: "NCBI RefSeq"
source_id: "gene-b1567"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1567"
  - "ydfW"
---

# ydfW

`gene.b1567`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1567`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfW (gene.b1567) is a gene entity. It encodes ydfW (protein.P76164). Encoded protein function: FUNCTION: May be involved in H(2) production during fermentative growth. {ECO:0000269|PubMed:24025676}. EcoCyc product frame: G6834-MONOMER. EcoCyc synonyms: intK. Genomic coordinates: 1647174-1647323. EcoCyc protein note: Overexpression of ydfW increases fitness as well as resistance to several antibiotics, including spiramycin and erythromycin . A ydfW null mutant was reported to produce less hydrogen than wild type under fermentation conditions. A ydfW expression clone from the ASKA library does not complement the phenotype . ydfW may represent a significantly truncated allele of a phage integrase. Note in ASAP: "N-terminal deletion of 1129 nucleotides relative to Escherichia coli ATCC 8739 (ASAP:AEM-0007804)."

## Biological Role

Repressed by dicA (protein.P06966). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76164|protein.P76164]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydfW; function=+
- `represses` <-- [[protein.P06966|protein.P06966]] `RegulonDB` `S` - regulator=DicA; target=ydfW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005236,ECOCYC:G6834,GeneID:946111`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1647174-1647323:-; feature_type=gene
