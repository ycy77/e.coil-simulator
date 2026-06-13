---
entity_id: "gene.b2349"
entity_type: "gene"
name: "intS"
source_database: "NCBI RefSeq"
source_id: "gene-b2349"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2349"
  - "intS"
---

# intS

`gene.b2349`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2349`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intS (gene.b2349) is a gene entity. It encodes intS (protein.P37326). Encoded protein function: FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. EcoCyc product frame: G7218-MONOMER. EcoCyc synonyms: intC, yfdB. Genomic coordinates: 2466545-2467702. EcoCyc protein note: IntS is the integrase required for both integration and excision of the prophage KpLE1 . A narrow concentration range of IntS enables excisive recombination . IntS binds DNA at the KplE1 attachment site attL . In the presence of their DNA target sites, IntS oligomers are stabilized . The attL site overlaps with the intS promoter region, thereby enabling negative autoregulation of intS expression by IntS .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37326|protein.P37326]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=intS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007756,ECOCYC:G7218,GeneID:946821`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2466545-2467702:+; feature_type=gene
