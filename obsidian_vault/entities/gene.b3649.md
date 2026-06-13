---
entity_id: "gene.b3649"
entity_type: "gene"
name: "rpoZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3649"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3649"
  - "rpoZ"
---

# rpoZ

`gene.b3649`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3649`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoZ (gene.b3649) is a gene entity. It encodes rpoZ (protein.P0A800). Encoded protein function: FUNCTION: Promotes RNA polymerase (RNAP) assembly. Latches the N- and C-terminal regions of the beta' subunit thereby facilitating its interaction with the beta and alpha subunits. {ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. EcoCyc product frame: EG10899-MONOMER. EcoCyc synonyms: spoS. Genomic coordinates: 3822106-3822381. EcoCyc protein note: RpoZ copurifies with RNA polymerase and may play a structural role in that complex. RpoZ copurifies with APORNAP-CPLX and, when added during renaturation studies, maximizes the yield of functional polymerase . RpoZ binds to RPOC-MONOMER, preventing its aggregation during renaturation and assisting in its addition to the partially formed polymerase complex . The initiating methionine of RpoZ is cleaved . Recombinant RpoZ is also cleaved by an endogenous protease, most likely by EG10673-MONOMER...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A800|protein.P0A800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rpoZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011933,ECOCYC:EG10899,GeneID:948160`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3822106-3822381:+; feature_type=gene
