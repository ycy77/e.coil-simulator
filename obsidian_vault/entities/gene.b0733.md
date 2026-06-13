---
entity_id: "gene.b0733"
entity_type: "gene"
name: "cydA"
source_database: "NCBI RefSeq"
source_id: "gene-b0733"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0733"
  - "cydA"
---

# cydA

`gene.b0733`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0733`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cydA (gene.b0733) is a gene entity. It encodes cydA (protein.P0ABJ9). Encoded protein function: FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:2656671, ECO:0000269|PubMed:6307994, ECO:0000269|PubMed:7577938}. EcoCyc product frame: CYDA-MONOMER. EcoCyc synonyms: cyd-1. Genomic coordinates: 771458-773026. EcoCyc protein note: cydA encodes subunit I of the cytochrome bd-I complex; it contains all three heme cofactors (heme b558, heme b595 and heme d) and is the site of ubiquinol oxidation and oxygen reduction . CydA contains the heme b558 component of cytochrome bd-I and is the site of ubiquinol oxidation . Purified, reconstituted CydA can be reduced by ubiquinol but it does not reduce molecular oxygen . The CydA protein has nine transmembrane helices, the N-terminus is located in the periplasm and the C-terminus in the cytoplasm ; in the bd-I complex, the subunit forms two four-helix bundles with an additional peripheral helix (see also )...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5), hns (protein.P0ACF8), nac (protein.Q47005). Activated by fnr (protein.P0A9E5), arcA (protein.P0A9Q1), cra (protein.P0ACP1), yjiE (protein.P39376), nac (protein.Q47005).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABJ9|protein.P0ABJ9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=cydA; function=-+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=cydA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=cydA; function=+
- `activates` <-- [[protein.P39376|protein.P39376]] `RegulonDB` `S` - regulator=HypT; target=cydA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cydA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=cydA; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=cydA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cydA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002499,ECOCYC:EG10173,GeneID:945341`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:771458-773026:+; feature_type=gene
