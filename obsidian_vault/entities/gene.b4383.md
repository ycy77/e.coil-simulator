---
entity_id: "gene.b4383"
entity_type: "gene"
name: "deoB"
source_database: "NCBI RefSeq"
source_id: "gene-b4383"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4383"
  - "deoB"
---

# deoB

`gene.b4383`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4383`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deoB (gene.b4383) is a gene entity. It encodes deoB (protein.P0A6K6). Encoded protein function: FUNCTION: Isomerase that catalyzes the conversion of deoxy-ribose 1-phosphate (dRib-1-P) and ribose 1-phosphate (Rib-1-P) to deoxy-ribose 5-phosphate (dRib-5-P) and ribose 5-phosphate (Rib-5-P), respectively. {ECO:0000255|HAMAP-Rule:MF_00740, ECO:0000269|PubMed:1089430, ECO:0000269|PubMed:4992818}. EcoCyc product frame: PPENTOMUT-MONOMER. EcoCyc synonyms: tlr, drm, thyR. Genomic coordinates: 4619603-4620826. EcoCyc protein note: Phosphopentomutase is a catabolic enzyme which catalyzes the transfer of a phosphate group between the C1 and the C5 carbon atoms of ribose and deoxyribose, respectively . A mutation in deoB suppresses the high thymine requirement for growth of thy mutants and improves the survival of thyA mutants in stationary phase . Transposon insertion mutations in deoB suppress the growth defect of a tktA tktB mutant . Deletion of deoB increases glycerol consumption as well as hydrogen and ethanol production compared to wild type , and increases lycopene production in an engineered strain . The deo operon has a complex pattern of regulation . Expression of deoB is downregulated by nitrogen starvation . The E...

## Biological Role

Repressed by modE (protein.P0A9G8), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), deoR (protein.P0ACK5), cytR (protein.P0ACN7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6K6|protein.P0A6K6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoB; function=-+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=deoB; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoB; function=-+
- `represses` <-- [[protein.P0ACK5|protein.P0ACK5]] `RegulonDB` `S` - regulator=DeoR; target=deoB; function=-
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=deoB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014377,ECOCYC:EG10220,GeneID:948910`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4619603-4620826:+; feature_type=gene
