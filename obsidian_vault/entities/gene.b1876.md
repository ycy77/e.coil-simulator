---
entity_id: "gene.b1876"
entity_type: "gene"
name: "argS"
source_database: "NCBI RefSeq"
source_id: "gene-b1876"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1876"
  - "argS"
---

# argS

`gene.b1876`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1876`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argS (gene.b1876) is a gene entity. It encodes argS (protein.P11875). Encoded protein function: Arginine--tRNA ligase (EC 6.1.1.19) (Arginyl-tRNA synthetase) (ArgRS) EcoCyc product frame: ARGS-MONOMER. EcoCyc synonyms: lov, lov-1. Genomic coordinates: 1960062-1961795. EcoCyc protein note: Arginine-tRNA ligase (ArgRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ArgRS belongs to the Class IA aminoacyl tRNA synthetases; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences . The kinetic mechanism of ArgRS has been investigated . ArgRS has been crystallized , and the structure of a complex with L-arginine has been solved at 2.9 Å resolution, elucidating the structural and fuctional role of active site residues . Conformational changes induced by interactions with its tRNA and arginine substrates have been studied , and specific interations with nucleotide residues in some tRNA species have been determined . Specificity determinants within tRNAArg that are important for recognition by ArgRS have been identified...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11875|protein.P11875]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argS; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006264,ECOCYC:EG10071,GeneID:946452`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1960062-1961795:+; feature_type=gene
