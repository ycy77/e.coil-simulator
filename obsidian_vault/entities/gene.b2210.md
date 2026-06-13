---
entity_id: "gene.b2210"
entity_type: "gene"
name: "mqo"
source_database: "NCBI RefSeq"
source_id: "gene-b2210"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2210"
  - "mqo"
---

# mqo

`gene.b2210`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2210`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mqo (gene.b2210) is a gene entity. It encodes mqo (protein.P33940). Encoded protein function: Malate:quinone oxidoreductase (EC 1.1.5.4) (MQO) (Malate dehydrogenase [quinone]) EcoCyc product frame: EG12069-MONOMER. EcoCyc synonyms: yojH. Genomic coordinates: 2305108-2306754. EcoCyc protein note: The mqo-encoded malate:quinone oxidoreductase (Mqo) is likely identical to the "malate oxidase" studied earlier . The membrane-associated enzyme catalyzes the oxidation of malate to oxaloacetate. Electrons are likely donated to the electron transfer chain at the quinone level. Contrary to earlier reports, Mqo and MALATE-DEHASE are active at the same time in the cell, although Mqo does not seem to play a significant physiological role in malate oxidation . Mqo activity is highest during exponential growth, decreases after the onset of stationary phase and is regulated by the carbon source . The ArcA-ArcB two-component system regulates mqo expression at the transcriptional level . An mqo deletion strain does not have an obvious growth defect, but mqo can partially substitute for the function of MALATE-DEHASE Mdh in an mdh mutant . Mqo: "malate:quinone oxidoreductase"

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33940|protein.P33940]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mqo; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=mqo; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=mqo; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007300,ECOCYC:EG12069,GeneID:946702`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2305108-2306754:-; feature_type=gene
