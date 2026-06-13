---
entity_id: "gene.b0978"
entity_type: "gene"
name: "appC"
source_database: "NCBI RefSeq"
source_id: "gene-b0978"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0978"
  - "appC"
---

# appC

`gene.b0978`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0978`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

appC (gene.b0978) is a gene entity. It encodes appC (protein.P26459). Encoded protein function: FUNCTION: A terminal oxidase that catalyzes quinol-dependent, Na(+)-independent oxygen uptake. Prefers menadiol over other quinols although ubiquinol was not tested (PubMed:8626304). Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:8626304}. EcoCyc product frame: APPC-MONOMER. EcoCyc synonyms: cbdA, cyxA. Genomic coordinates: 1037740-1039284. EcoCyc protein note: appC encodes subunit I of E. coli cytochrome bd-II; it contains all three heme cofactors and the quinol binding loop (Q loop) . AppC has 60% homology with the cofactor binding CYDA-MONOMER "CydA" subunit of CYT-D-UBIOX-CPLX . The AppB subunit harbors a structural UBIQUINONE-8 or DEMETHYLMENAQUINONE demethylmenaquinone-8 molecule.

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26459|protein.P26459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=appC; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003300,ECOCYC:EG11380,GeneID:945585`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1037740-1039284:+; feature_type=gene
