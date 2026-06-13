---
entity_id: "gene.b4060"
entity_type: "gene"
name: "yjcB"
source_database: "NCBI RefSeq"
source_id: "gene-b4060"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4060"
  - "yjcB"
---

# yjcB

`gene.b4060`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4060`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjcB (gene.b4060) is a gene entity. It encodes yjcB (protein.P32700). Encoded protein function: Uncharacterized protein YjcB EcoCyc product frame: EG11937-MONOMER. Genomic coordinates: 4274760-4275041. EcoCyc protein note: A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress . yjcB was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 compared to pH 7.6) as measured by ribosome coverage of its transcripts using RNA-Seq .

## Biological Role

Activated by soxR (protein.P0ACS2), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32700|protein.P32700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=yjcB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjcB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013300,ECOCYC:EG11937,GeneID:948569`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4274760-4275041:-; feature_type=gene
