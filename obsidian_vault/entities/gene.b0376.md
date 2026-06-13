---
entity_id: "gene.b0376"
entity_type: "gene"
name: "ampH"
source_database: "NCBI RefSeq"
source_id: "gene-b0376"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0376"
  - "ampH"
---

# ampH

`gene.b0376`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0376`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ampH (gene.b0376) is a gene entity. It encodes ampH (protein.P0AD70). Encoded protein function: FUNCTION: Hydrolyzes the cross-linked dimers tetrapentapeptide (D45) and tetratetrapeptide (D44). Removes the terminal D-alanine from muropeptides and disaccharide pentapeptide M5 with a C-terminal D-Ala-D-Ala dipeptide. Associated with recycling and remodeling of peptidoglycan (PG). Also displays a low beta-lactamase activity. {ECO:0000269|PubMed:22001512}. EcoCyc product frame: EG12867-MONOMER. EcoCyc synonyms: yaiH. Genomic coordinates: 395130-396287. EcoCyc protein note: AmpH is a penicillin-binding protein that catalyzes both DD-carboxypeptidase and DD-endopeptidase activities . AmpH is a bifunctional class C penicillin-binding protein with a probable role in peptidoglycan remodelling and/or recycling. AmpH binds a range of β-lactams, including penicillin G . Though AmpH is similar to class C β-lactamases, it has no detectable β-lactamase activity . AmpH may influence or contain a weak DD-carboxypeptidase activity . Purified AmpH cleaves the DD peptide bridge in cross-linked muropeptides in vitro . Purified AmpH removes the D-alanine from muropeptides with a C-terminal D-alanyl-D-alanine dipeptide . Purified AmpH binds Bocillin . AmpH has a 23-residue amino-terminal signal sequence which is cleaved in the mature protein . AmpH is membrane-associated...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD70|protein.P0AD70]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001292,ECOCYC:EG12867,GeneID:946904`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:395130-396287:-; feature_type=gene
