---
entity_id: "gene.b0820"
entity_type: "gene"
name: "ybiT"
source_database: "NCBI RefSeq"
source_id: "gene-b0820"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0820"
  - "ybiT"
---

# ybiT

`gene.b0820`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0820`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiT (gene.b0820) is a gene entity. It encodes ybiT (protein.P0A9U3). Encoded protein function: FUNCTION: Involved in peptide bond synthesis. Allows translation of proteins with poly-acidic sequences in the middle of the protein, which otherwise cause intrinsic ribosome destabilization (IRD) due to difficulties in maintaining an intact ribosome. {ECO:0000269|PubMed:38661232}. EcoCyc product frame: G6423-MONOMER. Genomic coordinates: 855963-857555. EcoCyc protein note: YbiT belongs to the YbiT subfamily of the ABCF family of ATP-binding cassette (ABC) proteins . There are four ABCF family proteins within E. coli K-12: YheS, YJJK-MONOMER "EttA", UUP-MONOMER "Uup" and G6423-MONOMER "YbiT", all of which are involved in noncanonical translation of 'hard-to-translate' nascent peptides getting them through the ribosome exit tunnel. YheS represses poly-acidic sequence-dependent intrinsic ribosome destabilization, stalling and premature termination . Overexpression of an EQ2 mutant of YbiT (carrying substitutions in the predicted ATPase active sites) of E. coli CFT073 inhibits protein synthesis . Accumulation of the cationic fluorescent dye 3,3'-dipropylthiadicarbocyanine iodide (diS-C3) is greater in ybiT knockout cells compared to wild type...

## Biological Role

Repressed by lrp (protein.P0ACJ0), ascG (protein.P24242).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9U3|protein.P0A9U3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P24242|protein.P24242]] `RegulonDB` `S` - regulator=AscG; target=ybiT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002801,ECOCYC:G6423,GeneID:945440`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:855963-857555:+; feature_type=gene
