---
entity_id: "gene.b4395"
entity_type: "gene"
name: "ytjC"
source_database: "NCBI RefSeq"
source_id: "gene-b4395"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4395"
  - "ytjC"
---

# ytjC

`gene.b4395`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4395`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytjC (gene.b4395) is a gene entity. It encodes gpmB (protein.P0A7A2). Encoded protein function: Probable phosphoglycerate mutase GpmB (EC 5.4.2.-) (PGAM) (Phosphoglyceromutase) EcoCyc product frame: PGAM2-MONOMER. EcoCyc synonyms: gpmB. Genomic coordinates: 4633797-4634444. EcoCyc protein note: YtjC was identified as a member of the phosphoglycerate mutase B subfamily; however, no members of that family have been functionally characterized , and were unable to detect phosphoglycerate mutase activity in vitro. Members of this family may in fact be acid phosphatases . Unpurified YtjC has phosphatase activity against 6-phosphobenzisoxazole and p-nitrophenyl phosphate . YtjC is a multicopy suppressor of the conditional ΔEG10945 serB phenotype . The intrinsic phosphoserine phosphatase activity of YtjC is extremely low; mutants with increased activity have been selected . The 14 enzymes involved in glycolysis have hundreds of unique protein-protein interactions (PPIs) with at least 237 other protein interactors, most of which are not essential and about half of the interactors are other enzymes. Six of the glycolytic enzymes (Pgk, GpmA, GpmI, PykA, GapA and Eno) have at least 1 uncharacterized interactor, while Eno has 5 interactors. There were no uncharacterized interactors identified for GpmB .

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7A2|protein.P0A7A2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014416,ECOCYC:EG12164,GeneID:948918`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4633797-4634444:+; feature_type=gene
