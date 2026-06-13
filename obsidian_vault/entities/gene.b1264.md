---
entity_id: "gene.b1264"
entity_type: "gene"
name: "trpE"
source_database: "NCBI RefSeq"
source_id: "gene-b1264"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1264"
  - "trpE"
---

# trpE

`gene.b1264`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1264`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpE (gene.b1264) is a gene entity. It encodes trpE (protein.P00895). Encoded protein function: FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. {ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:4886289, ECO:0000269|PubMed:5333199}. EcoCyc product frame: ANTHRANSYNCOMPI-MONOMER. EcoCyc synonyms: anth, tryD, tryp-4. Genomic coordinates: 1321384-1322946.

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00895|protein.P00895]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpE; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpE; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004244,ECOCYC:EG11028,GeneID:945846`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1321384-1322946:-; feature_type=gene
