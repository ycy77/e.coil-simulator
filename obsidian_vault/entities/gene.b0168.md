---
entity_id: "gene.b0168"
entity_type: "gene"
name: "map"
source_database: "NCBI RefSeq"
source_id: "gene-b0168"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0168"
  - "map"
---

# map

`gene.b0168`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0168`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

map (gene.b0168) is a gene entity. It encodes map (protein.P0AE18). Encoded protein function: FUNCTION: Removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). Requires deformylation of the N(alpha)-formylated initiator methionine before it can be hydrolyzed. {ECO:0000255|HAMAP-Rule:MF_01974, ECO:0000269|PubMed:20521764, ECO:0000269|PubMed:3027045}. EcoCyc product frame: EG10570-MONOMER. Genomic coordinates: 188712-189506. EcoCyc protein note: All known proteins in E. coli use N-formyl methionine (N-fMet) as the first amino acid in a peptide chain. Amino-terminal maturation involves two enzymes, EG11440-MONOMER (PDF) which removes the formyl group, and methionine aminopeptidase (MAP), which catalyzes the removal of the deformylated methionine residue . Oxidation of N-terminal fMet prevents hydrolysis by MAP as determined using bottom-up proteomics . MAP interacts directly with the ribosome at the ribosomal exit tunnel and competes with EG11440-MONOMER for overlapping sites . MAP does not interfere with binding of EG11003-MONOMER trigger factor or SRP-CPLX SRP to translating ribosomes...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), gcvB (gene.b4443), fur (protein.P0A9A9). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE18|protein.P0AE18]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=map; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=map; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=map; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000571,ECOCYC:EG10570,GeneID:947882`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:188712-189506:-; feature_type=gene
