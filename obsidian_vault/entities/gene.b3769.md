---
entity_id: "gene.b3769"
entity_type: "gene"
name: "ilvM"
source_database: "NCBI RefSeq"
source_id: "gene-b3769"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3769"
  - "ilvM"
---

# ilvM

`gene.b3769`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3769`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvM (gene.b3769) is a gene entity. It encodes ilvM (protein.P0ADG1). Encoded protein function: Acetolactate synthase isozyme 2 small subunit (EC 2.2.1.6) (ALS-II) (Acetohydroxy-acid synthase II small subunit) (AHAS-II) EcoCyc product frame: SMALLILVM-MONOMER. Genomic coordinates: 3952201-3952464. EcoCyc protein note: Acetohydroxyacid synthase II (AHAS II) encoded by ilvG and ilvM catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate and α-acetolactate. AHAS II is not found in E. coli K-12 due to a mutation in ilvG, although it is found in other E. coli strains. See the entry for G8221-MONOMER for more information. In non-K-12 strains AHAS II is a bifunctional enzyme that catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate for the isoleucine pathway and of α-acetolactate for the valine pathway . Both the large catalytic subunit IlvG and the small regulatory subunit IlvM are required for this activity, though the exact stoichiometry of the IlvM subunit is unclear . The kinetics of AHAS II have been evaluated .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

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

- `encodes` --> [[protein.P0ADG1|protein.P0ADG1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvM; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012313,ECOCYC:EG10501,GeneID:948279`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3952201-3952464:+; feature_type=gene
