---
entity_id: "gene.b3386"
entity_type: "gene"
name: "rpe"
source_database: "NCBI RefSeq"
source_id: "gene-b3386"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3386"
  - "rpe"
---

# rpe

`gene.b3386`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3386`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpe (gene.b3386) is a gene entity. It encodes rpe (protein.P0AG07). Encoded protein function: FUNCTION: Catalyzes the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02227, ECO:0000269|PubMed:21402925}. EcoCyc product frame: RIBULP3EPIM-MONOMER. EcoCyc synonyms: dod, yhfD. Genomic coordinates: 3514382-3515059. EcoCyc protein note: Ribulose-5-phosphate 3-epimerase (Rpe) is an enzyme of the non-oxidative branch of the pentose phosphate pathway. Rpe requires ferrous iron for activity and is vulnerable to damage by H2O2 due to Fenton chemistry. Mn2+, Co2+ and Zn2+ can substitute for Fe2+ to varying degrees, and Rpe containing these alternative cations is not vulnerable to H2O2. Induction of the manganese transporter can protect Rpe from H2O2 damage . An rpe mutant strain does not grow on minimal medium containing either ribose or xylose, but grows when both sugars are present . rpe mutant strains have a growth defect in complex medium and a more severe growth defect in minimal medium containing glycolytic carbon sources or gluconate . A mutation in rpe, drsE30, supresses the temperature-sensitive growth defect of the dnaR130 mutant allele . Review:

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG07|protein.P0AG07]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpe; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011061,ECOCYC:M004,GeneID:947896`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3514382-3515059:-; feature_type=gene
