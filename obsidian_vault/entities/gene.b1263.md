---
entity_id: "gene.b1263"
entity_type: "gene"
name: "trpD"
source_database: "NCBI RefSeq"
source_id: "gene-b1263"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1263"
  - "trpD"
---

# trpD

`gene.b1263`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1263`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpD (gene.b1263) is a gene entity. It encodes trpGD (protein.P00904). Encoded protein function: FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. In addition to synthesizing anthranilate, it also catalyzes the second step of the pathway, the transfer of the phosphoribosyl group of 5-phosphorylribose-1-pyrophosphate (PRPP) to anthranilate. {ECO:0000269|PubMed:2428387, ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:5333199}. EcoCyc product frame: ANTHRANSYNCOMPII-MONOMER. EcoCyc synonyms: trpGD. Genomic coordinates: 1319789-1321384. EcoCyc protein note: Anthranilate phosphoribosyl transferase (TrpD) catalyzes the second step in the pathway of tryptophan biosynthesis. TrpD catalyzes a phosphoribosyltransferase reaction that generates N-(5'-phosphoribosyl)-anthranilate...

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00904|protein.P00904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpD; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpD; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004241,ECOCYC:EG11027,GeneID:945109`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1319789-1321384:-; feature_type=gene
