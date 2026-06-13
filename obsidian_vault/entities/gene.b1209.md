---
entity_id: "gene.b1209"
entity_type: "gene"
name: "lolB"
source_database: "NCBI RefSeq"
source_id: "gene-b1209"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1209"
  - "lolB"
---

# lolB

`gene.b1209`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1209`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lolB (gene.b1209) is a gene entity. It encodes lolB (protein.P61320). Encoded protein function: FUNCTION: Plays a critical role in the incorporation of lipoproteins in the outer membrane after they are released by the LolA protein. Essential for E.coli viability. EcoCyc product frame: EG11293-MONOMER. EcoCyc synonyms: hemM, ychC. Genomic coordinates: 1262877-1263500. EcoCyc protein note: LolB is an outer membrane lipoprotein which is part of the 5 protein LolABCDE lipoprotein trafficking pathway; LolB interacts with G6465-MONOMER "LolA"-lipoprotein complexes and catalyses lipoprotein insertion into the outer membrane. The major outer membrane lipoprotein Lpp, is incorporated into proteoliposomes reconstituted from purified LolB and phospholipids in vitro; Lpp is transferred from Lpp-LolA to a water-soluble LolB (mLolB) in vitro . Lipoproteins (Lpp, Pal and NlpB) released from spheroplasts in the presence of LolA are subsequently incorporated into LolB-containing membranes in vitro . LolB specifically interacts with liganded LolA and the interaction between free LolA and LolB is negligible...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61320|protein.P61320]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004059,ECOCYC:EG11293,GeneID:945775`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1262877-1263500:-; feature_type=gene
