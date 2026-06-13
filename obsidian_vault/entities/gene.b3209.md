---
entity_id: "gene.b3209"
entity_type: "gene"
name: "elbB"
source_database: "NCBI RefSeq"
source_id: "gene-b3209"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3209"
  - "elbB"
---

# elbB

`gene.b3209`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3209`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elbB (gene.b3209) is a gene entity. It encodes elbB (protein.P0ABU5). Encoded protein function: FUNCTION: Displays glyoxalase activity, catalyzing the conversion of glyoxal to glycolate (PubMed:26678554). However, this apparent glyoxalase activity may reflect a protein deglycase activity, which could be the primary function of this protein like other DJ-1 superfamily members such as PARK7, YajL, YhbO and HchA (Probable). Is not able to use methylglyoxal as substrate (PubMed:26678554). {ECO:0000269|PubMed:26678554, ECO:0000305}. EcoCyc product frame: EG11383-MONOMER. EcoCyc synonyms: yzzB, elb2, s27a, yhbL. Genomic coordinates: 3349806-3350459. EcoCyc protein note: ElbB belongs to the DJ-1/ThiJ/PfpI superfamily of proteins . A crystal structure has been solved at 1.65 Å resolution , and the predicted functional site somewhat resembles that of the human protein DJ-1 . The protein exhibits low glyoxalase activity with glyoxal, but not methylglyoxal, as the substrate . The ElbB protein cross-reacts with an antibody prepared against a peptide of the 2.2 region of σ70 and σ32 and was therefore originally named sigma cross-reacting protein 27A (SCRP-27A) . elbB was identified in a mutant screen designed to identify genes involved in the biosynthesis of isopentenyl diphosphate, a precursor of isoprenoids...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABU5|protein.P0ABU5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010532,ECOCYC:EG11383,GeneID:947903`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3349806-3350459:-; feature_type=gene
