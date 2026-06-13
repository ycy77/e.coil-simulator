---
entity_id: "gene.b3321"
entity_type: "gene"
name: "rpsJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3321"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3321"
  - "rpsJ"
---

# rpsJ

`gene.b3321`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3321`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsJ (gene.b3321) is a gene entity. It encodes rpsJ (protein.P0A7R5). Encoded protein function: FUNCTION: Involved in the binding of tRNA to the ribosomes (PubMed:6759118). Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). In complex with NusB is involved in the regulation of ribosomal RNA (rRNA) biosynthesis by transcriptional antitermination. S10 binds RNA non-specifically and increases the affinity of NusB for the boxA RNA sequence (PubMed:11884128, PubMed:16109710, PubMed:7678781). S10 may constitute the critical antitermination component of the NusB-S10 complex (PubMed:19111659). {ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:6759118, ECO:0000269|PubMed:7678781}. EcoCyc product frame: EG10909-MONOMER. EcoCyc synonyms: nusE. Genomic coordinates: 3452959-3453270. EcoCyc protein note: The S10 protein (NusE) is a component of the 30S subunit of the ribosome...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7R5|protein.P0A7R5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsJ; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rpsJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010862,ECOCYC:EG10909,GeneID:947816`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3452959-3453270:-; feature_type=gene
