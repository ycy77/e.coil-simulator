---
entity_id: "gene.b0037"
entity_type: "gene"
name: "caiC"
source_database: "NCBI RefSeq"
source_id: "gene-b0037"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0037"
  - "caiC"
---

# caiC

`gene.b0037`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0037`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiC (gene.b0037) is a gene entity. It encodes caiC (protein.P31552). Encoded protein function: FUNCTION: Catalyzes the transfer of CoA to carnitine, generating the initial carnitinyl-CoA needed for the CaiB reaction cycle. Also has activity toward crotonobetaine and gamma-butyrobetaine. {ECO:0000255|HAMAP-Rule:MF_01524, ECO:0000269|PubMed:18266698}. EcoCyc product frame: CAIC-MONOMER. EcoCyc synonyms: yaaM. Genomic coordinates: 36271-37824. EcoCyc protein note: Carnitine-CoA ligase (CaiC) catalyzes the transfer of CoA to carnitine. CaiC was initially predicted to have CoA ligase activity by . In vitro, the enzyme can utilize both L- and D-carnitine as well as crotonobetaine and γ-butyrobetaine as substrates. CaiC also exhibits a CoA-transferase-like activity in vitro, which can not substitute for CaiB activity in vivo .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31552|protein.P31552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiC; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000133,ECOCYC:EG11558,GeneID:944886`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:36271-37824:-; feature_type=gene
