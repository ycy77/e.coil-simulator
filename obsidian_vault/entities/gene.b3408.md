---
entity_id: "gene.b3408"
entity_type: "gene"
name: "feoA"
source_database: "NCBI RefSeq"
source_id: "gene-b3408"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3408"
  - "feoA"
---

# feoA

`gene.b3408`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3408`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

feoA (gene.b3408) is a gene entity. It encodes feoA (protein.P0AEL3). Encoded protein function: FUNCTION: Involved in Fe(2+) ion uptake (PubMed:8407793). Does not stimulate the GTPase activity of the N-terminus of FeoB (residues 1-276). {ECO:0000269|PubMed:23104801, ECO:0000269|PubMed:8407793}. EcoCyc product frame: EG12101-MONOMER. Genomic coordinates: 3540163-3540390. EcoCyc protein note: FeoA is part of a conserved ferrous iron transport system. The function of this protein has not yet been determined in E. coli; however, in a number of orthologous systems, FeoA was shown to form a complex with the FeoB transmembrane transporter component. A solution structure of FeoA shows a Src-homology 3 (SH3)-like fold; the protein forms a β-barrel with two α-helices, one of which is positioned over the barrel. FeoA does not appear to act as a GTPase-activating protein for FeoB . A feoA::Tn5 mutant shows partially reduced uptake of ferrous iron . Fe2+ uptake is regulated by Fur; a Fur binding site is located upstream of the feo locus . feo expression is low under aerobic condtions and increases under anaerobic conditions under the positive control of transcription factors ArcA and FNR; Feo-mediated import of Fe2+ promotes Fur-Fe2+ occupancy amd contributes to Fur regulation under anaerobic conditions . Overexpression of feoA increases the tolerance of E. coli to n-butanol...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1). Activated by fnr (protein.P0A9E5), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEL3|protein.P0AEL3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=feoA; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=feoA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=feoA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=feoA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011124,ECOCYC:EG12101,GeneID:947909`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3540163-3540390:+; feature_type=gene
