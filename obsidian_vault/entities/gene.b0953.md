---
entity_id: "gene.b0953"
entity_type: "gene"
name: "rmf"
source_database: "NCBI RefSeq"
source_id: "gene-b0953"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0953"
  - "rmf"
---

# rmf

`gene.b0953`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0953`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rmf (gene.b0953) is a gene entity. It encodes rmf (protein.P0AFW2). Encoded protein function: FUNCTION: During stationary phase, converts 70S ribosomes to an immature dimeric form (90S ribosomes) which are converted to inactive 100S ribosomes (a process called ribosomal hibernation) by the hibernation promoting factor HPF (PubMed:18174192, PubMed:7677746). Inactivates ribosomes by covering the peptidyl transferase (PTase) center of the 23S rRNA and the entrance of peptide exit tunnel (PubMed:12473202, PubMed:15066119). However crystallization with T.thermophilus 70S ribosomes shows it binds near the 3'-end of the 16S rRNA near the anti-Shine-Dalgarno sequence, where it would sterically hinder translation initiation (PubMed:22605777). In this crystal binding of RMF induces movement of the 30S head domain away from the rest of the ribosome, presumably so they would more easily form dimers (PubMed:22605777). Also involved in protection against heat stress, but this role is not dependent on the maintenance of ribosome dimers (PubMed:15278243). {ECO:0000255|HAMAP-Rule:MF_00919, ECO:0000269|PubMed:12473202, ECO:0000269|PubMed:15066119, ECO:0000269|PubMed:15278243, ECO:0000269|PubMed:18174192, ECO:0000269|PubMed:19170772, ECO:0000269|PubMed:7677746, ECO:0000269|PubMed:8440252, ECO:0000269|PubMed:9278503}. EcoCyc product frame: EG50004-MONOMER. EcoCyc synonyms: res, rimF...

## Biological Role

Repressed by CueR-Cu+ (complex.ecocyc.CPLX0-10393), ZntR-Zn2+ (complex.ecocyc.CPLX0-10394), DNA-binding transcriptional dual regulator KdpE-phosphorylated (complex.ecocyc.CPLX0-7795), NhaR-Na+ DNA-binding transcriptional activator (complex.ecocyc.MONOMER0-46), nhaR (protein.P0A9G2), cueR (protein.P0A9G4), arcA (protein.P0A9Q1), zntR (protein.P0ACS5), and 3 more. Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), sdiA (protein.P07026), slyA (protein.P0A8W2), fur (protein.P0A9A9), crp (protein.P0ACJ8), rcdA (protein.P75811), mcbR (protein.P76114).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFW2|protein.P0AFW2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (18)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=rmf; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=rmf; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=rmf; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rmf; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=rmf; function=+
- `activates` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=rmf; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-10393|complex.ecocyc.CPLX0-10393]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-10394|complex.ecocyc.CPLX0-10394]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7795|complex.ecocyc.CPLX0-7795]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.MONOMER0-46|complex.ecocyc.MONOMER0-46]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=rmf; function=-
- `represses` <-- [[protein.P0A9G4|protein.P0A9G4]] `RegulonDB` `S` - regulator=CueR; target=rmf; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rmf; function=-
- `represses` <-- [[protein.P0ACS5|protein.P0ACS5]] `RegulonDB` `S` - regulator=ZntR; target=rmf; function=-
- `represses` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rmf; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `S` - regulator=KdpE; target=rmf; function=-
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB|EcoCyc` `S` - regulator=PhoP; target=rmf; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003227,ECOCYC:EG50004,GeneID:945567`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1015715-1015882:+; feature_type=gene
