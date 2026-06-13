---
entity_id: "gene.b3612"
entity_type: "gene"
name: "gpmM"
source_database: "NCBI RefSeq"
source_id: "gene-b3612"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3612"
  - "gpmM"
---

# gpmM

`gene.b3612`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3612`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpmM (gene.b3612) is a gene entity. It encodes gpmI (protein.P37689). Encoded protein function: FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate (2-PGA) and 3-phosphoglycerate (3-PGA). {ECO:0000269|PubMed:10437801}. EcoCyc product frame: PGMI-MONOMER. EcoCyc synonyms: gpmC, pgmI, gpmI, yibO. Genomic coordinates: 3785260-3786804. EcoCyc protein note: E. coli contains both a 2,3-bisphosphoglyerate-dependent phosphoglycerate mutase (dPGM, GpmA) and this cofactor-independent phosphoglycerate mutase (PGMI-MONOMER GpmM, also called iPGM). The GpmM enzyme has significantly lower specific activity . Differential inhibition by vanadate allowed independent measurement of both enzymes during the E. coli growth cycle . A gpmM deletion strain does not have a growth defect under the conditions tested, while a gpmA gpmM double mutant strain does not appear to be viable. The growth phenotype of a gpmA mutant can be rescued by expression of gpmM from a medium-copy plasmid . gpmM shows differential codon adaptation, resulting in differential translation efficiency signatures in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. A gpmM deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37689|protein.P37689]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=gpmM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011818,ECOCYC:EG12296,GeneID:948130`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3785260-3786804:+; feature_type=gene
