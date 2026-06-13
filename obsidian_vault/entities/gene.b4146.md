---
entity_id: "gene.b4146"
entity_type: "gene"
name: "epmB"
source_database: "NCBI RefSeq"
source_id: "gene-b4146"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4146"
  - "epmB"
---

# epmB

`gene.b4146`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4146`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

epmB (gene.b4146) is a gene entity. It encodes epmB (protein.P39280). Encoded protein function: FUNCTION: With EpmA is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. EpmB appears to act before EpmA. Displays lysine 2,3-aminomutase activity, producing (R)-beta-lysine from (S)-alpha-lysine (L-lysine). Cannot use (S)-ornithine or (R)-alpha-lysine as a substrate. {ECO:0000269|PubMed:17042480, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:22128152}. EcoCyc product frame: G7836-MONOMER. EcoCyc synonyms: yjeK. Genomic coordinates: 4374629-4375657. EcoCyc protein note: Co-expression of EpmB enhances the lysylation of EF-P by EpmA in vivo. EpmB may catalyze the conversion of α-lysyl-EF-P to β-lysyl-EF-P , but preliminary evidence indicates that it acts before EpmA . The epmB gene product is similar to the lysine 2,3-aminomutase of Clostridium subterminale, although phylogenetic clustering has shown that EpmB belongs to a different subfamily than the lysine 2,3-aminomutases . The purified protein has low lysine 2,3-aminomutase activity and produces (R)-β-lysine, the enantiomer of the product of the Clostridium enzyme. The low activity of the E. coli enzyme compared to the clostridial enzyme may indicate that L-lysine is not its natural substrate, or that β-lysine is required in low amounts...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39280|protein.P39280]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013580,ECOCYC:G7836,GeneID:948662`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4374629-4375657:-; feature_type=gene
