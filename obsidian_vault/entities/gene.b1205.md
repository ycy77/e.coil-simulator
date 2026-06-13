---
entity_id: "gene.b1205"
entity_type: "gene"
name: "ychH"
source_database: "NCBI RefSeq"
source_id: "gene-b1205"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1205"
  - "ychH"
---

# ychH

`gene.b1205`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1205`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychH (gene.b1205) is a gene entity. It encodes ychH (protein.P0AB49). Encoded protein function: Uncharacterized protein YchH EcoCyc product frame: EG11533-MONOMER. Genomic coordinates: 1258791-1259069. EcoCyc protein note: YchH is involved in the cellular response to hydrogen peroxide and cadmium stress . A ychH mutant is much more sensitive to hydrogen peroxide and cadmium stress than wild type and shows increased biofilm formation. In a metabolically engineered strain that expresses genes required for the degradation of cis-dichloroethylene (cis-DCE), ychH expression is induced. Moreover, YchH is important for degradation of cis-DCE . CRP functions as a Class II activator at the ychH promoter . EG11533 was significantly upregulated in simulated microgravity .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB49|protein.P0AB49]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ychH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=ychH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004049,ECOCYC:EG11533,GeneID:945762`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1258791-1259069:+; feature_type=gene
