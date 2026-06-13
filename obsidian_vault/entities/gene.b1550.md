---
entity_id: "gene.b1550"
entity_type: "gene"
name: "gnsB"
source_database: "NCBI RefSeq"
source_id: "gene-b1550"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1550"
  - "gnsB"
---

# gnsB

`gene.b1550`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1550`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gnsB (gene.b1550) is a gene entity. It encodes gnsB (protein.P77695). Encoded protein function: FUNCTION: Overexpression increases levels of unsaturated fatty acids and suppresses both the temperature-sensitive fabA6 mutation and cold-sensitive secG null mutation. {ECO:0000269|PubMed:11544213}. EcoCyc product frame: G6823-MONOMER. EcoCyc synonyms: ydfY. Genomic coordinates: 1637609-1637782. EcoCyc protein note: GnsB and its homolog MONOMER0-1701 GnsA affect unsaturated fatty acid abundance and membrane fluidity . Multicopy expression of gnsA or gnsB suppresses secG null or fabA6 mutant growth phenotypes. GnsA and GnsB overproduction causes greater abundance of unsaturated fatty acids in a secG mutant background and results in phenotypes consistent with greater membrane fluidity. A gnsA gnsB double mutant does not exhibit any obvious growth phenotypes . GnsB and GnsA are also able to rescue the growth defect and to restore the relative proportion of unsaturated to saturated fatty acids in various (p)ppGpp-deficient strains (e.g. deletion mutants of EG10281, EG10835 and EG10966) at low temperatures . GnsA and GnsB are not subject to cold shock regulation. Wild-type expression of GnsB is below the limit of detection . GnsB: "secG null mutant suppressor B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77695|protein.P77695]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005177,ECOCYC:G6823,GeneID:946054`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1637609-1637782:-; feature_type=gene
