---
entity_id: "gene.b0564"
entity_type: "gene"
name: "appY"
source_database: "NCBI RefSeq"
source_id: "gene-b0564"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0564"
  - "appY"
---

# appY

`gene.b0564`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0564`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

appY (gene.b0564) is a gene entity. It encodes appY (protein.P05052). Encoded protein function: FUNCTION: Induces the synthesis of acid phosphatase (AppA) and several other polypeptides (such as AppBC) during the deceleration phase of growth. It also acts as a transcriptional repressor for one group of proteins that are synthesized preferentially in exponential growth and for one group synthesized only in the stationary phase. Also involved in the stabilization of the sigma stress factor RpoS during stress conditions. {ECO:0000269|PubMed:18383615}. EcoCyc product frame: PD00967. Genomic coordinates: 583681-584430. EcoCyc protein note: The AppY, "acid phosphatase," transcriptional regulator induces the expression of energy metabolism genes under anaerobiosis, stationary phase, and phosphate starvation. Under these same conditions, the expression of the appY gene is induced . The genes regulated by AppY have promoters that are recognized by both σ70 and σ38; AppY activates their transcription when any of these σ factors is bound to the RNA polymerase . The specific AppY binding site has not yet been identified. When AppY is overproduced, the expression of 30 proteins is induced or repressed in a growth phase-dependent fashion. Overproduction of AppY also causes an elevated spontaneous mutation rate...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05052|protein.P05052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=appY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001929,ECOCYC:EG10050,GeneID:948797`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:583681-584430:+; feature_type=gene
