---
entity_id: "gene.b0085"
entity_type: "gene"
name: "murE"
source_database: "NCBI RefSeq"
source_id: "gene-b0085"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0085"
  - "murE"
---

# murE

`gene.b0085`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0085`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murE (gene.b0085) is a gene entity. It encodes murE (protein.P22188). Encoded protein function: FUNCTION: Catalyzes the addition of meso-diaminopimelic acid to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (UMAG) in the biosynthesis of bacterial cell-wall peptidoglycan. Is also able to use many meso-diaminopimelate analogs as substrates, although much less efficiently, but not L-lysine. {ECO:0000269|PubMed:11124264, ECO:0000269|PubMed:2269304, ECO:0000269|PubMed:3905407}. EcoCyc product frame: UDP-NACMURALGLDAPLIG-MONOMER. Genomic coordinates: 93166-94653. EcoCyc protein note: UDP-N-acetylmuramoylalanyl-D-glutamate 2,6-diaminopimelate ligase (MurE) catalyzes the addition of the third amino acid, meso-diaminopimelate, to the peptide moiety of the monomer unit of peptidoglycan . The enzyme's ability to use the LL-DAP isomer at a low level leads to the incorporation of LL-DAP into peptidoglycan in a DIAMINOPIMEPIM-MONOMER (dapF) mutant . A crystal structure of the enzyme has been solved at 2Å resolution, allowing the identification of residues involved in catalysis. The Lys224 residue within the active site is carbamylated , and this modification appears to be required for enzymatic activity . Temperature-sensitive murE mutants have been isolated , and the genetic defects of the murE1 allele has been identified...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22188|protein.P22188]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=murE; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=murE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000311,ECOCYC:EG10621,GeneID:944791`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:93166-94653:+; feature_type=gene
