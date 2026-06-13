---
entity_id: "gene.b0923"
entity_type: "gene"
name: "mukE"
source_database: "NCBI RefSeq"
source_id: "gene-b0923"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0923"
  - "mukE"
---

# mukE

`gene.b0923`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0923`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mukE (gene.b0923) is a gene entity. It encodes mukE (protein.P22524). Encoded protein function: FUNCTION: Involved in chromosome condensation, segregation and cell cycle progression. May participate in facilitating chromosome segregation by condensation DNA from both sides of a centrally located replisome during cell division. Probably acts via its interaction with MukB and MukF. {ECO:0000269|PubMed:8602138}. EcoCyc product frame: EG11252-MONOMER. EcoCyc synonyms: kicA, ycbA. Genomic coordinates: 975622-976326. EcoCyc protein note: MukE plays a role in chromosome partitioning during cell division . The effect of MukE on chromosome partitioning may be due to a role in DNA topology or condensation . MukF (the kleisin) and MukE (the kleisin-interacting winged-helix tandem element, "KITE") are proposed to be a toxin-antitoxin pair, respectively . Published reports disagree about whether or not the MukE protein is essential for viability. A mukE mutant is reported to exhibit heat sensitivity and formation of anucleate products of cell division . A mukE mutant also exhibits increased sensitivity to novobiocin, compared to wild type . A mukE mutant exhibits a defect in wild-type localization of MukB to nucleoid-associated foci . A mukF mutation suppresses the observed inviability of a mukE mutant...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22524|protein.P22524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=mukE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003136,ECOCYC:EG11252,GeneID:945550`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:975622-976326:+; feature_type=gene
