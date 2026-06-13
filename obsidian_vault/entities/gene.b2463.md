---
entity_id: "gene.b2463"
entity_type: "gene"
name: "maeB"
source_database: "NCBI RefSeq"
source_id: "gene-b2463"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2463"
  - "maeB"
---

# maeB

`gene.b2463`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2463`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

maeB (gene.b2463) is a gene entity. It encodes maeB (protein.P76558). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of malate to pyruvate (PubMed:17557829). In vitro, shows malolactic enzyme activity in the presence of NADPH. However, it is unlikely that this activity is of relevance in E.coli, which produces little NADPH (PubMed:33824210). {ECO:0000269|PubMed:17557829, ECO:0000269|PubMed:33824210}. EcoCyc product frame: MALIC-NADP-MONOMER. EcoCyc synonyms: ypfF. Genomic coordinates: 2576098-2578377. EcoCyc protein note: E. coli encodes two "malic enzymes" that catalyze the decarboxylation of malate to form pyruvate with concomitant reduction of NAD(P)+. One enzyme, MaeB (described here) reduces NADP+, while the other, MALIC-NAD-MONOMER MaeA, reduces NAD+ . MaeB activity is highly regulated by key metabolites . Inhibition by acetyl-CoA may direct carbon distribution at the PEP-pyruvate-oxaloacetate metabolic node . MaeB appears to be important for supplying NADPH during growth on two-carbon compounds ; flux-balance analysis predicts flux to pyruvate through MaeB during growth on acetate . Metabolic flux through the malic enzymes during growth on glycerol as the sole source of carbon appears to be essentially zero...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76558|protein.P76558]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=maeB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008111,ECOCYC:G7293,GeneID:946947`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2576098-2578377:-; feature_type=gene
