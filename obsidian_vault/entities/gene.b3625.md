---
entity_id: "gene.b3625"
entity_type: "gene"
name: "waaY"
source_database: "NCBI RefSeq"
source_id: "gene-b3625"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3625"
  - "waaY"
---

# waaY

`gene.b3625`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3625`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaY (gene.b3625) is a gene entity. It encodes waaY (protein.P27240). Encoded protein function: FUNCTION: Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS). Catalyzes the phosphorylation of the second heptose unit (HepII) of the inner core. {ECO:0000250|UniProtKB:Q9ZIS7}. EcoCyc product frame: EG11425-MONOMER. EcoCyc synonyms: rfaY. Genomic coordinates: 3800267-3800965. EcoCyc protein note: WaaY is a heptose specific lipopolysaccharide (LPS) core kinase which catalyses phosphorylation of the second heptose residue in the inner core of LPS . Non-polar inactivation of waaY in the non K-12 E. coli strain F470 (CPD-21352 "R1 core type") results in a minor increase in sensitivity to novobiocin and SDS and the core oligosaccharide of this mutant is not phosphorylated on heptose II . WaaY activity is dependent on prior WaaP, WaaQ (and possibly WaaG ) function; the core oligosaccharide of both waaP and waaQ mutants does not have a phosphoryl substituent on heptose II despite the presence of functional waaY . Inactivation of waaY produces a phenotype of decreased susceptibility to the human cathelicidin antimicrobial peptide (LL-37); reduced peptide binding to the cell surface and a diminished capacity to compromise the inner membrane were observed...

## Biological Role

Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27240|protein.P27240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaY; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=waaY; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=waaY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011856,ECOCYC:EG11425,GeneID:948145`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3800267-3800965:-; feature_type=gene
