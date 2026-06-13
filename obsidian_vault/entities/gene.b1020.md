---
entity_id: "gene.b1020"
entity_type: "gene"
name: "phoH"
source_database: "NCBI RefSeq"
source_id: "gene-b1020"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1020"
  - "phoH"
---

# phoH

`gene.b1020`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1020`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoH (gene.b1020) is a gene entity. It encodes phoH (protein.P0A9K1). Encoded protein function: Protein PhoH (Phosphate starvation-inducible protein PsiH) EcoCyc product frame: EG11734-MONOMER. EcoCyc synonyms: psiH. Genomic coordinates: 1084992-1086056. EcoCyc protein note: The purified PhoH protein has ATP binding activity . PhoH has similarity to the N-terminal domain of superfamily I helicases . A phoH mutant strain was tested in a phenotype microarray experiment . Expression of phoH is inducible by phosphate starvation .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1), glaR (protein.P37338), nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9K1|protein.P0A9K1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phoH; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=phoH; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=phoH; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=phoH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=phoH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=phoH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003458,ECOCYC:EG11734,GeneID:948010`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1084992-1086056:+; feature_type=gene
