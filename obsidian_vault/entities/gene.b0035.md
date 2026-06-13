---
entity_id: "gene.b0035"
entity_type: "gene"
name: "caiE"
source_database: "NCBI RefSeq"
source_id: "gene-b0035"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0035"
  - "caiE"
---

# caiE

`gene.b0035`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0035`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiE (gene.b0035) is a gene entity. It encodes caiE (protein.P39206). Encoded protein function: FUNCTION: Overproduction of CaiE stimulates the activity of CaiB and CaiD. {ECO:0000269|PubMed:7815937}. EcoCyc product frame: CAIE-MONOMER. Genomic coordinates: 34781-35371. EcoCyc protein note: The function of the CaiE protein is currently unknown. Overproduction of CaiE appears to stimulate carnitine racemase activity of CaiD and carnitine dehydratase activity of CaiB, leading to the hypothesis that CaiE may be involved in the synthesis or activation of an unknown cofactor required for these activities .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39206|protein.P39206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiE; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000128,ECOCYC:EG12608,GeneID:948999`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:34781-35371:-; feature_type=gene
