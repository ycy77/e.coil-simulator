---
entity_id: "gene.b0474"
entity_type: "gene"
name: "adk"
source_database: "NCBI RefSeq"
source_id: "gene-b0474"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0474"
  - "adk"
---

# adk

`gene.b0474`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0474`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adk (gene.b0474) is a gene entity. It encodes adk (protein.P69441). Encoded protein function: FUNCTION: Catalyzes the reversible transfer of the terminal phosphate group between ATP and AMP. Plays an important role in cellular energy homeostasis and in adenine nucleotide metabolism. {ECO:0000255|HAMAP-Rule:MF_00235, ECO:0000269|PubMed:166976, ECO:0000269|PubMed:6243627}. EcoCyc product frame: ADENYL-KIN-MONOMER. EcoCyc synonyms: dnaW, plsA. Genomic coordinates: 497175-497819. EcoCyc protein note: Adenylate kinase is an essential enzyme required for the biosynthesis of purine ribonucleotides and has a key role in controlling the rate of cell growth . Adenylate kinase is a relatively small, monomeric protein that consists of three functionally relevant domains: the N-terminal nucleotide binding (NMPbind) domain that binds AMP, followed by the CORE domain that represents the bulk of the enzyme and encloses the LID domain that binds ATP. There are estimated to be approximately 10,000 molecules of adenylate kinase present in the cell . Adenylate kinase activity may be inhibited by interaction with the phosphorylated form of PTSH-MONOMER HPr and the ribosome . Various crystal and solution structures of the enzyme have been solved, and a reaction mechanism was proposed and refined...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69441|protein.P69441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001645,ECOCYC:EG10032,GeneID:945097`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:497175-497819:+; feature_type=gene
