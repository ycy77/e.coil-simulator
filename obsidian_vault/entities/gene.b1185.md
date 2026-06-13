---
entity_id: "gene.b1185"
entity_type: "gene"
name: "dsbB"
source_database: "NCBI RefSeq"
source_id: "gene-b1185"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1185"
  - "dsbB"
---

# dsbB

`gene.b1185`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1185`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsbB (gene.b1185) is a gene entity. It encodes dsbB (protein.P0A6M2). Encoded protein function: FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by oxidizing the DsbA protein. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:22267510, ECO:0000269|PubMed:7688471, ECO:0000269|PubMed:8430071}. EcoCyc product frame: MONOMER0-4142. EcoCyc synonyms: ycgA, roxB, dsbX, iarB, rosB. Genomic coordinates: 1232500-1233030. EcoCyc protein note: DsbB is a protein thiol:quinone oxidoreductase that functions within a pathway for protein disulfide bond formation; DsbB catalyses the oxidation of DsbA via the reduction of membrane quinones; DsbB, in conjunction with membrane quinones generates disulfide bonds de novo and is considered to be a disulfide bond manufacturer within E. coli K-12 (reviewed in ). DsbB null mutants (dsbB::kan5) synthesize OmpA and β-lactamase proteins that are deficient in disulfide bonds and this defect can be rescued by supplementation with cystine or oxidized glutathione; DsbA is present in the fully reduced state in DsbB null mutants (see also )...

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6M2|protein.P0A6M2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=dsbB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003979,ECOCYC:EG11393,GeneID:946344`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1232500-1233030:-; feature_type=gene
