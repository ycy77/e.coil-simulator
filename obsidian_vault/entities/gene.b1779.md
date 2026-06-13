---
entity_id: "gene.b1779"
entity_type: "gene"
name: "gapA"
source_database: "NCBI RefSeq"
source_id: "gene-b1779"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1779"
  - "gapA"
---

# gapA

`gene.b1779`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1779`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gapA (gene.b1779) is a gene entity. It encodes gapA (protein.P0A9B2). Encoded protein function: FUNCTION: Catalyzes the oxidative phosphorylation of glyceraldehyde 3-phosphate (G3P) to 1,3-bisphosphoglycerate (BPG) using the cofactor NAD. The first reaction step involves the formation of a hemiacetal intermediate between G3P and a cysteine residue, and this hemiacetal intermediate is then oxidized to a thioester, with concomitant reduction of NAD to NADH. The reduced NADH is then exchanged with the second NAD, and the thioester is attacked by a nucleophilic inorganic phosphate to produce BPG. {ECO:0000269|PubMed:2659073}. EcoCyc product frame: GAPDH-A-MONOMER. EcoCyc synonyms: gad, gap1. Genomic coordinates: 1862771-1863766.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9B2|protein.P0A9B2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gapA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=gapA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=gapA; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=gapA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005920,ECOCYC:EG10367,GeneID:947679`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1862771-1863766:+; feature_type=gene
