---
entity_id: "gene.b3774"
entity_type: "gene"
name: "ilvC"
source_database: "NCBI RefSeq"
source_id: "gene-b3774"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3774"
  - "ilvC"
---

# ilvC

`gene.b3774`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3774`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvC (gene.b3774) is a gene entity. It encodes ilvC (protein.P05793). Encoded protein function: FUNCTION: Involved in the biosynthesis of branched-chain amino acids (BCAA). Catalyzes an alkyl-migration followed by a ketol-acid reduction of (S)-2-acetolactate (S2AL) to yield (R)-2,3-dihydroxy-isovalerate. In the isomerase reaction, S2AL is rearranged via a Mg-dependent methyl migration to produce 3-hydroxy-3-methyl-2-ketobutyrate (HMKB). In the reductase reaction, this 2-ketoacid undergoes a metal-dependent reduction by NADPH to yield (R)-2,3-dihydroxy-isovalerate. Also able to use 2-ketopantoate, 2-ketoisovalerate, 2-ketovalerate, 2-ketobutyrate, 3-hydroxypyruvate, 3-hydroxy-2-ketobutyrate and pyruvate (PubMed:15654896). {ECO:0000269|PubMed:15654896, ECO:0000269|PubMed:21515217, ECO:0000269|PubMed:2653423, ECO:0000269|PubMed:9015391}. EcoCyc product frame: KETOLREDUCTOISOM-MONOMER. Genomic coordinates: 3957970-3959445.

## Biological Role

Activated by rpoD (protein.P00579), ilvY (protein.P05827).

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

- `encodes` --> [[protein.P05793|protein.P05793]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvC; function=+
- `activates` <-- [[protein.P05827|protein.P05827]] `RegulonDB` `C` - regulator=IlvY; target=ilvC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012331,ECOCYC:EG10495,GeneID:948286`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3957970-3959445:+; feature_type=gene
