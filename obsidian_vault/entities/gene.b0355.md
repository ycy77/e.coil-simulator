---
entity_id: "gene.b0355"
entity_type: "gene"
name: "frmB"
source_database: "NCBI RefSeq"
source_id: "gene-b0355"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0355"
  - "frmB"
---

# frmB

`gene.b0355`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0355`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frmB (gene.b0355) is a gene entity. It encodes frmB (protein.P51025). Encoded protein function: FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against two pNP-esters (pNP-acetate and pNP-propionate), alpha-naphthyl acetate and lactoylglutathione. {ECO:0000269|PubMed:16567800}. EcoCyc product frame: G6208-MONOMER. EcoCyc synonyms: yaiM. Genomic coordinates: 377535-378368. EcoCyc protein note: FrmB is a promiscuous serine hydrolase; its highest specific activity is with the substrate S-formylglutathione. Sulfhydryl inhibitors affect enzymatic activity . FrmB is encoded in an operon with FrmR and FrmA, which are proteins involved in the oxidation of formaldehyde. FrmB has similarity to the S-formylglutathione hydrolase of Paracoccus denitrificans and a paralog, YeiG . Formaldehyde stimulates expression of frmB 45-fold in wild type and 70-fold in a yeiG deletion background. Under normal growth conditions, neither a frmB deletion mutant nor a frmB yeiG double mutant have a detectable growth defect. Addition of 0.4 mM formaldehyde to the growth medium caused only a small growth defect in the frmB single mutant, while the growth rate of the double mutant drops to 43% of wild type...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), frmR (protein.P0AAP3).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P51025|protein.P51025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AAP3|protein.P0AAP3]] `RegulonDB` `S` - regulator=FrmR; target=frmB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001219,ECOCYC:G6208,GeneID:944991`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:377535-378368:-; feature_type=gene
