---
entity_id: "gene.b3630"
entity_type: "gene"
name: "waaP"
source_database: "NCBI RefSeq"
source_id: "gene-b3630"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3630"
  - "waaP"
---

# waaP

`gene.b3630`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3630`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaP (gene.b3630) is a gene entity. It encodes waaP (protein.P25741). Encoded protein function: FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (By similarity). Catalyzes the phosphorylation of heptose I (HepI), the first heptose added to the Kdo2-lipid A module (By similarity). {ECO:0000250|UniProtKB:Q9R9D6}. EcoCyc product frame: EG11340-MONOMER. EcoCyc synonyms: rfaP. Genomic coordinates: 3805153-3805950. EcoCyc protein note: WaaP is a heptose specific lipopolysaccharide (LPS) core kinase; it is required for the addition of phosphate to O-4 of the first heptose residue in the core oligosaccharide of LPS . waaP is highly conserved in E. coli strains with K-12, R1, R2, R3 and R4 core types and between E. coli and Salmonella typhimurium . Non-polar inactivation of waaP in the non K-12 E. coli strain F470 (CPD-21352 "R1 core type") results in hypersensitivity to novobiocin and SDS; the core oligosaccharide of this mutant (which contains functional waaQ and waaY) lacks all phosphoryl substituents and a heptose III residue indicating that WaaP function is a prerequisite for EG11341-MONOMER "WaaQ" and EG11425-MONOMER "WaaY" activity (see also ). Non-polar inactivation of EG11339 "waaG" (encoding LPS glucosyltransferase) in E...

## Biological Role

Activated by rpoD (protein.P00579), yiaU (protein.P37682).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25741|protein.P25741]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaP; function=+
- `activates` <-- [[protein.P37682|protein.P37682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011866,ECOCYC:EG11340,GeneID:948150`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3805153-3805950:-; feature_type=gene
