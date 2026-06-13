---
entity_id: "gene.b1217"
entity_type: "gene"
name: "chaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1217"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1217"
  - "chaB"
---

# chaB

`gene.b1217`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1217`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chaB (gene.b1217) is a gene entity. It encodes chaB (protein.P0AE63). Encoded protein function: FUNCTION: Might be a regulator of the sodium-potassium/proton antiporter ChaA. {ECO:0000250|UniProtKB:P0AE65}. EcoCyc product frame: EG12402-MONOMER. Genomic coordinates: 1272119-1272349. EcoCyc protein note: ChaB is predicted to be a regulator of cation transport. The solution structure of ChaB shows a fold also found in the cyclin-box family of proteins . ChaB has an important role in maintaining antibiotic tolerance under starvation; chaB is upregulated during nutrient starvation and the starvation-induced ampicillin tolerance levels of a chaB knockout strain are significantly reduced over both a 6 and 30 day period .

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE63|protein.P0AE63]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=chaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004087,ECOCYC:EG12402,GeneID:945792`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1272119-1272349:+; feature_type=gene
