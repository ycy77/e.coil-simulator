---
entity_id: "gene.b0811"
entity_type: "gene"
name: "glnH"
source_database: "NCBI RefSeq"
source_id: "gene-b0811"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0811"
  - "glnH"
---

# glnH

`gene.b0811`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0811`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnH (gene.b0811) is a gene entity. It encodes glnH (protein.P0AEQ3). Encoded protein function: FUNCTION: Involved in a glutamine-transport system GlnHPQ. {ECO:0000269|PubMed:3027504}. EcoCyc product frame: GLNH-MONOMER. Genomic coordinates: 847258-848004. EcoCyc protein note: GlnH is the periplasmic binding protein of an L-glutamine ABC transport system. Early studies reported the purification of a glutamine binding protein released by cold osmotic shock treatment of whole cells of E. coli K12 and K10 derived strains . glnH encodes a periplasmic L-glutamine binding protein that is required for growth on L-glutamine as sole carbon source . Purified GlnH binds L-glutamine with µM affinity (KD = 5 x 10-7M) ; L-glutamine binding induces conformational change in the protein . Purifed, crystallized GlnH consists of two globular domains connected by two peptide linkers (hinges); glutamine binds in a cleft between the two domains; binding induces large scale movement of the two hinges and the ligand is completely buried within the protein

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by lrp (protein.P0ACJ0), glnG (protein.P0AFB8), zraR (protein.P14375).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEQ3|protein.P0AEQ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnH; function=-+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=glnH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnH; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002771,ECOCYC:EG10386,GeneID:944872`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:847258-848004:-; feature_type=gene
