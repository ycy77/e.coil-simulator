---
entity_id: "gene.b3661"
entity_type: "gene"
name: "nlpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3661"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3661"
  - "nlpA"
---

# nlpA

`gene.b3661`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3661`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nlpA (gene.b3661) is a gene entity. It encodes nlpA (protein.P04846). Encoded protein function: Lipoprotein 28 EcoCyc product frame: EG10657-MONOMER. Genomic coordinates: 3839175-3839993. EcoCyc protein note: NlpA is an inner membrane lipoprotein in Escherichia coli; NlpA is non-essential for growth . NlpA may serve as an L and D-methionine receptor, feeding inefficiently into the METNIQ-METHIONINE-ABC-CPLX "methionine ABC transporter". Compared to a wild type strain and a ΔmetQ single mutant, a ΔmetQ ΔnlpA double mutant grows poorly with D-methionine (and to a lesser extent with L-methionine) as sole sulfur source and takes up labeled L-methionine and labeled D-methionine poorly . NlpA expressed from a plasmid can complement a ΔnlpA ΔmetQ ΔmetE triple mutation for growth on D-methionine . NlpA may play a role in virulence of enteropathogenic strains of E. coli . An E. coli DH5α nlpA::Tn5 mutant produces significantly less outer membrane vesicles than the wild type . This phenotype is most severe in late log phase and stationary phase . E. coli ΔnlpA ΔdegP double mutants have a severe stress dependent synthetic growth defect .

## Biological Role

Repressed by glaR (protein.P37338). Activated by csgD (protein.P52106).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04846|protein.P04846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=nlpA; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=nlpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011964,ECOCYC:EG10657,GeneID:948175`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3839175-3839993:-; feature_type=gene
