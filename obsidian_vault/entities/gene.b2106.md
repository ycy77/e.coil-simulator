---
entity_id: "gene.b2106"
entity_type: "gene"
name: "rcnA"
source_database: "NCBI RefSeq"
source_id: "gene-b2106"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2106"
  - "rcnA"
---

# rcnA

`gene.b2106`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2106`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcnA (gene.b2106) is a gene entity. It encodes rcnA (protein.P76425). Encoded protein function: FUNCTION: Efflux system for nickel and cobalt. {ECO:0000269|PubMed:15805538}. EcoCyc product frame: G7138-MONOMER. EcoCyc synonyms: yohM. Genomic coordinates: 2185917-2186741. EcoCyc protein note: RcnA is an inner membrane efflux system for nickel and cobalt ions. Under aerobic growth conditions deletion of rcnA results in decreased resistance to nickel and cobalt and increased intracellular accumulation of Ni2+ can be directly demonstrated . rcnA expressed in trans in a strain lacking chromosomal rcnA results in increased resistance to Ni2+ and Co2+ compared to wild type . RcnA is involved in Ni2+ homeostasis under anaerobic conditions and at low nickel concentrations (10nM Ni2+). Under these conditions deletion of rcnA results in reduced nickel accumulation and decreased HYDROG3-CPLX activity. Deletion of rcnA results in increased EG11519-MONOMER "NikR" activity which impacts nickel import via the high affinity ABC-20-CPLX . RcnA contains 6 predicted transmembrane regions and a histidine rich domain in the center of the protein that may be associated with nickel binding Exposure of rcnA mutants to subinhibitory concentrations of nickel promotes the formation of biofilm structure . rcnA expression is regulated by the G7137-MONOMER "RcnR transcritional repressor"...

## Biological Role

Repressed by rcnR (protein.P64530).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76425|protein.P76425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P64530|protein.P64530]] `RegulonDB` `S` - regulator=RcnR; target=rcnA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006968,ECOCYC:G7138,GeneID:949078`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2185917-2186741:+; feature_type=gene
