---
entity_id: "gene.b0797"
entity_type: "gene"
name: "rhlE"
source_database: "NCBI RefSeq"
source_id: "gene-b0797"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0797"
  - "rhlE"
---

# rhlE

`gene.b0797`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0797`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhlE (gene.b0797) is a gene entity. It encodes rhlE (protein.P25888). Encoded protein function: FUNCTION: DEAD-box RNA helicase involved in ribosome assembly. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. May play a role in the interconversion of ribosomal RNA-folding intermediates that are further processed by DeaD or SrmB during ribosome maturation. {ECO:0000255|HAMAP-Rule:MF_00968, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:18083833}. EcoCyc product frame: EG11235-MONOMER. Genomic coordinates: 830872-832236. EcoCyc protein note: RhlE is a ribosome-associated factor that may be involved in ribosome maturation . RhlE is a member of the DEAD-box-containing ATP-dependent RNA helicase family . Its ATPase activity is stimulated by both long RNAs and short oligoribonucleotides . Of the three E. coli DEAD-box RNA helicases DeaD, SrmB and RhlE, only RhlE can unwind substrates with short or no single-stranded extensions, but the enzyme shows low processivity . RhlE physically interacts with EG10690-MONOMER and EG10859-MONOMER . RhlE can functionally replace RhlB within the degradosome . An rhlE mutant does not have any obvious growth defect . Overexpression of RhlE can substitute for the essential function of DeaD during cold shock , but exacerbates the cold-sensitive growth defect of an srmB mutant...

## Biological Role

Activated by cecR (protein.P0ACU0).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25888|protein.P25888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACU0|protein.P0ACU0]] `RegulonDB` `C` - regulator=CecR; target=rhlE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002719,ECOCYC:EG11235,GeneID:945425`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:830872-832236:+; feature_type=gene
