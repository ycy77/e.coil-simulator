---
entity_id: "gene.b3826"
entity_type: "gene"
name: "yigL"
source_database: "NCBI RefSeq"
source_id: "gene-b3826"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3826"
  - "yigL"
---

# yigL

`gene.b3826`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3826`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yigL (gene.b3826) is a gene entity. It encodes yigL (protein.P27848). Encoded protein function: FUNCTION: Phosphosugar phosphatase that plays a crucial role in the sugar-phosphate stress response (PubMed:23582330, PubMed:23873911). Catalyzes the hydrolysis of phosphosugars, which are toxic and can inhibit growth at high concentrations, thus promoting their efflux (Probable). In addition, it exhibits strong activity against pyridoxine phosphate (PNP) and pyridoxal phosphate (PLP) (PubMed:39133002). It plays an important role in maintaining PNP and PLP homeostasis (PubMed:39133002). It may play a role when cells face high intracellular PNP levels (PubMed:39133002). Control of PNP levels is crucial because PNP has the potential to inhibit PLP-dependent enzymes and proteins (PubMed:39133002). YigL helps alleviate PNP toxicity by reducing intracellular PNP concentrations, and contributes significantly, in combination with YbhA, to PLP dephosphorylation (PubMed:39133002). It is therefore a primary enzyme in the regulation of vitamin B(6) metabolism (PubMed:39133002)...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27848|protein.P27848]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yigL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012500,ECOCYC:EG11470,GeneID:2847768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4010200-4011000:+; feature_type=gene
