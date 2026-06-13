---
entity_id: "gene.b1593"
entity_type: "gene"
name: "bidA"
source_database: "NCBI RefSeq"
source_id: "gene-b1593"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1593"
  - "bidA"
---

# bidA

`gene.b1593`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1593`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bidA (gene.b1593) is a gene entity. It encodes bioD2 (protein.P0A6E9). Encoded protein function: FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. {ECO:0000255|HAMAP-Rule:MF_00336}. EcoCyc product frame: G6851-MONOMER. EcoCyc synonyms: ynfK. Genomic coordinates: 1666524-1667219.

## Biological Role

Repressed by mlc (protein.P50456), nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fnr (protein.P0A9E5), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6E9|protein.P0A6E9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bidA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=bidA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=bidA; function=+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=bidA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bidA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005319,ECOCYC:G6851,GeneID:944927`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1666524-1667219:-; feature_type=gene
