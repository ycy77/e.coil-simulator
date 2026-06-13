---
entity_id: "gene.b0526"
entity_type: "gene"
name: "cysS"
source_database: "NCBI RefSeq"
source_id: "gene-b0526"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0526"
  - "cysS"
---

# cysS

`gene.b0526`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0526`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysS (gene.b0526) is a gene entity. It encodes cysS (protein.P21888). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys) (PubMed:12662918). Unable to bind serine (PubMed:12662918). {ECO:0000269|PubMed:12662918}.; FUNCTION: In addition to its role as an aminoacyl-tRNA synthetase, has also cysteine persulfide synthase activity. Produces reactive persulfide species such as cysteine persulfide (CysSSH) from substrate cysteine and mediate direct incorporation of CysSSH into proteins during translations, resulting in protein persulfides and polysulfides (PubMed:29079736). CysSSHs behave as potent antioxidants and cellular protectants (PubMed:29079736). {ECO:0000269|PubMed:29079736}. EcoCyc product frame: CYSS-MONOMER. EcoCyc synonyms: syc. Genomic coordinates: 554611-555996. EcoCyc protein note: Cysteine-tRNA ligase (CysRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. CysRS belongs to the Class I aminoacyl tRNA synthetases . CysRS is a monomer in solution . The N-terminal domain of CysRS is active in adenylate synthesis, while the C-terminal domain is able to bind and discriminate tRNA...

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21888|protein.P21888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cysS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cysS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001810,ECOCYC:EG10196,GeneID:946969`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:554611-555996:+; feature_type=gene
