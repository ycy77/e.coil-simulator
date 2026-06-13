---
entity_id: "gene.b0893"
entity_type: "gene"
name: "serS"
source_database: "NCBI RefSeq"
source_id: "gene-b0893"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0893"
  - "serS"
---

# serS

`gene.b0893`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0893`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

serS (gene.b0893) is a gene entity. It encodes serS (protein.P0A8L1). Encoded protein function: FUNCTION: Catalyzes the attachment of serine to tRNA(Ser) (PubMed:7537870). Is also able to aminoacylate tRNA(Sec) with serine, to form the misacylated tRNA L-seryl-tRNA(Sec), which will be further converted into selenocysteinyl-tRNA(Sec). {ECO:0000269|PubMed:2963963, ECO:0000269|PubMed:7537870, ECO:0000269|PubMed:8065908}. EcoCyc product frame: SERS-MONOMER. Genomic coordinates: 939428-940720. EcoCyc protein note: Serine-tRNA ligase (SerRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. SerRS belongs to the Class II aminoacyl tRNA synthetases, which share three regions of homology . SerRS is a dimer in solution . Specificity determinants within tRNASer that are important for recognition by SerRS have been identified . SerRS also aminoacylates a special tRNA, tRNASec, with serine . The charging efficiency for tRNASec is approximately 1% of that for tRNASer . The serine residue of Ser-tRNASec is subsequently converted to selenocysteine by CPLX0-1141. tRNASec recognizes the stop codon UGA...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8L1|protein.P0A8L1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=serS; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003038,ECOCYC:EG10947,GeneID:945506`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:939428-940720:+; feature_type=gene
