---
entity_id: "gene.b3092"
entity_type: "gene"
name: "uxaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3092"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3092"
  - "uxaC"
---

# uxaC

`gene.b3092`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3092`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uxaC (gene.b3092) is a gene entity. It encodes uxaC (protein.P0A8G3). Encoded protein function: Uronate isomerase (EC 5.3.1.12) (Glucuronate isomerase) (Uronic isomerase) EcoCyc product frame: UXAC-MONOMER. EcoCyc synonyms: ygjY, ygjX, ygjZ. Genomic coordinates: 3243329-3244741. EcoCyc protein note: Uronate isomerase catalyzes the initial step of isomerization of the alduronic to the keturonic acid in the glucuronate and galacturonate degradation pathways. Cofactor requirements of the enzyme are unclear; one of the earlier reports on purification of the enzyme states that Zn2+ inhibits the enzyme , while a later report states that uronate isomerase is a metalloenzyme, with Zn2+ as the likely physiologically relevant cofactor . Tagaturonate and fructuronate act as inducers ; production of the enzyme is under catabolite repression .

## Biological Role

Repressed by nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8G3|protein.P0A8G3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=uxaC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=uxaC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010167,ECOCYC:G81,GeneID:947599`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3243329-3244741:-; feature_type=gene
