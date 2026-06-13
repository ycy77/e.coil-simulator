---
entity_id: "gene.b1982"
entity_type: "gene"
name: "amn"
source_database: "NCBI RefSeq"
source_id: "gene-b1982"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1982"
  - "amn"
---

# amn

`gene.b1982`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1982`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amn (gene.b1982) is a gene entity. It encodes amn (protein.P0AE12). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of AMP to form adenine and ribose 5-phosphate. Involved in regulation of AMP concentrations. {ECO:0000255|HAMAP-Rule:MF_01932, ECO:0000269|PubMed:7000783}. EcoCyc product frame: AMP-NUCLEOSID-MONOMER. Genomic coordinates: 2055061-2056515.

## Biological Role

Repressed by nac (protein.Q47005). Activated by phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE12|protein.P0AE12]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=amn; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006579,ECOCYC:EG10039,GeneID:946508`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2055061-2056515:+; feature_type=gene
