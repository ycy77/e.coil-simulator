---
entity_id: "gene.b3771"
entity_type: "gene"
name: "ilvD"
source_database: "NCBI RefSeq"
source_id: "gene-b3771"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3771"
  - "ilvD"
---

# ilvD

`gene.b3771`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3771`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvD (gene.b3771) is a gene entity. It encodes ilvD (protein.P05791). Encoded protein function: FUNCTION: Functions in the biosynthesis of branched-chain amino acids. Catalyzes the dehydration of (2R,3R)-2,3-dihydroxy-3-methylpentanoate (2,3-dihydroxy-3-methylvalerate) into 2-oxo-3-methylpentanoate (2-oxo-3-methylvalerate) and of (2R)-2,3-dihydroxy-3-methylbutanoate (2,3-dihydroxyisovalerate) into 2-oxo-3-methylbutanoate (2-oxoisovalerate), the penultimate precursor to L-isoleucine and L-valine, respectively. {ECO:0000269|PubMed:13727223, ECO:0000269|PubMed:8325851}. EcoCyc product frame: DIHYDROXYACIDDEHYDRAT-MONOMER. Genomic coordinates: 3953478-3955328.

## Biological Role

Repressed by gcvB (gene.b4443), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05791|protein.P05791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvD; function=+
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=ilvD; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012318,ECOCYC:EG10496,GeneID:948277`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3953478-3955328:+; feature_type=gene
