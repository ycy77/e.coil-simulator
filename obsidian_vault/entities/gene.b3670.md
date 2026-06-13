---
entity_id: "gene.b3670"
entity_type: "gene"
name: "ilvN"
source_database: "NCBI RefSeq"
source_id: "gene-b3670"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3670"
  - "ilvN"
---

# ilvN

`gene.b3670`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3670`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvN (gene.b3670) is a gene entity. It encodes ilvN (protein.P0ADF8). Encoded protein function: Acetolactate synthase isozyme 1 small subunit (EC 2.2.1.6) (Acetohydroxy-acid synthase I small subunit) (AHAS-I) (ALS-I) EcoCyc product frame: SMALLILVN-MONOMER. Genomic coordinates: 3850802-3851092. EcoCyc protein note: IlvN is the small regulatory subunit of AHAS I, the bifunctional acetohydroxybutanoate synthase/acetolactate synthase which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. IlvN was shown to bind close to the FAD binding site of IlvB . The interactions between the large and small subunits from different isozymes were investigated . Wild type cells are sensitive to exogenous valine due to inhibition of the enzymatic activity of IlvB/N . ilvN mutants, however, while still able to grow in the absence of valine and isoleucine, are no longer sensitive in this manner to exogenous valine . The solution structure of IlvN in both the free and valine-bound form was determined by NMR methods. In its free form, IlvN exists as a mixture of conformational states, while in its bound form, IlvN exists as a single conformer . The backbone and side-chain assignments of IlvN in the valine bound form was reported .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADF8|protein.P0ADF8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvN; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ilvN; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ilvN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011997,ECOCYC:EG10502,GeneID:948183`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3850802-3851092:-; feature_type=gene
