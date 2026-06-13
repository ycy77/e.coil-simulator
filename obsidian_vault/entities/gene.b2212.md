---
entity_id: "gene.b2212"
entity_type: "gene"
name: "alkB"
source_database: "NCBI RefSeq"
source_id: "gene-b2212"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2212"
  - "alkB"
---

# alkB

`gene.b2212`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2212`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alkB (gene.b2212) is a gene entity. It encodes alkB (protein.P05050). Encoded protein function: FUNCTION: Dioxygenase that repairs alkylated DNA and RNA containing 3-methylcytosine or 1-methyladenine by oxidative demethylation. Has highest activity towards 3-methylcytosine. Has lower activity towards alkylated DNA containing ethenoadenine, and no detectable activity towards 1-methylguanine or 3-methylthymine. Accepts double-stranded and single-stranded substrates. Requires molecular oxygen, alpha-ketoglutarate and iron. Provides extensive resistance to alkylating agents such as MMS and DMS (SN2 agents), but not to MMNG and MNU (SN1 agents). {ECO:0000269|PubMed:12226668, ECO:0000269|PubMed:12594517, ECO:0000269|PubMed:16482161, ECO:0000269|PubMed:19706517, ECO:0000269|PubMed:20084272, ECO:0000269|PubMed:21068844}. EcoCyc product frame: EG10037-MONOMER. EcoCyc synonyms: aidD. Genomic coordinates: 2308691-2309341. EcoCyc protein note: AlkB is an Fe(II)-containing, 2-oxoglutarate-dependent dioxygenase which catalyses the non-mutagenic repair of methyl lesions in DNA and RNA. Purified AlkB is a 2-oxoglutarate and Fe(II) dependent dioxygenase which accurately repairs 1-methyladenine and 3-methylcytosine lesions in DNA (see also )...

## Biological Role

Repressed by ada (protein.P06134). Activated by ada (protein.P06134), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05050|protein.P05050]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `C` - regulator=Ada; target=alkB; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=alkB; function=+
- `represses` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `C` - regulator=Ada; target=alkB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007308,ECOCYC:EG10037,GeneID:946708`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2308691-2309341:-; feature_type=gene
