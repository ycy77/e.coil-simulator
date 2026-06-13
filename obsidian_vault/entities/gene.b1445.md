---
entity_id: "gene.b1445"
entity_type: "gene"
name: "ortT"
source_database: "NCBI RefSeq"
source_id: "gene-b1445"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1445"
  - "ortT"
---

# ortT

`gene.b1445`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1445`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ortT (gene.b1445) is a gene entity. It encodes ortT (protein.P64453). Encoded protein function: FUNCTION: Acts as an orphan toxin which is important for maintaining cell fitness during stress related to the stringent response (decreased amino acid, purine and thymidine availability). Overexpression inhibits cell growth and increases the formation of persister cells. Causes 99.9% of cells to undergo bacterial lysis within 2 hours after induction; nucleoids condense, the cytoplasm seems empty and the periplasmic space enlarges. The intracellular ATP level decreases about 27-fold suggesting the membrane potential may be disrupted. {ECO:0000269|PubMed:25643179}. EcoCyc product frame: G6756-MONOMER. EcoCyc synonyms: ydcX. Genomic coordinates: 1517389-1517562. EcoCyc protein note: ortT encodes a protein toxin that damages the cell membrane and reduces the intracellular ATP level. ortT is activated under conditions that induce the stringent response (eg. serine hydroxamate treatment) and may function to reduce growth during nutritional stress. OrtT reduces cell growth and metabolism in response to the stringent response induced by tetrahydrofolate (THF) depletion. Production of OrtT from a plasmid causes severe growth inhibition in LB medium; production of OrtT increases persistance - a dormant non-metabolizing state in which cells are tolerant to antibiotics...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64453|protein.P64453]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ortT; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ortT; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ortT; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ortT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004818,ECOCYC:G6756,GeneID:945936`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1517389-1517562:+; feature_type=gene
