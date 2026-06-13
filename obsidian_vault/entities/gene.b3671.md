---
entity_id: "gene.b3671"
entity_type: "gene"
name: "ilvB"
source_database: "NCBI RefSeq"
source_id: "gene-b3671"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3671"
  - "ilvB"
---

# ilvB

`gene.b3671`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3671`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvB (gene.b3671) is a gene entity. It encodes ilvB (protein.P08142). Encoded protein function: Acetolactate synthase isozyme 1 large subunit (AHAS-I) (EC 2.2.1.6) (Acetohydroxy-acid synthase I large subunit) (ALS-I) EcoCyc product frame: LARGEILVB-MONOMER. Genomic coordinates: 3851096-3852784. EcoCyc protein note: IlvB is the large catalytic subunit of AHAS I, the bifunctional acetohydroxybutanoate synthase/acetolactate synthase which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvB subunit can catalyze the reaction in isolation and is not inhibited by valine in the manner of the holoenzyme. However, the Vmax for the reaction as catalyzed by IlvB alone is sharply reduced, as is the enzyme's affinity for the required FAD cofactor . Both activities are catalyzed by the same active site on IlvB . The interactions between the large and small subunits from different isozymes were investigated .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

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

- `encodes` --> [[protein.P08142|protein.P08142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ilvB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011999,ECOCYC:EG10494,GeneID:948182`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3851096-3852784:-; feature_type=gene
