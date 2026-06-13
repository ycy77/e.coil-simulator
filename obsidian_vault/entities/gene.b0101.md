---
entity_id: "gene.b0101"
entity_type: "gene"
name: "yacG"
source_database: "NCBI RefSeq"
source_id: "gene-b0101"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0101"
  - "yacG"
---

# yacG

`gene.b0101`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0101`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yacG (gene.b0101) is a gene entity. It encodes yacG (protein.P0A8H8). Encoded protein function: FUNCTION: Inhibits all the catalytic activities of DNA gyrase by preventing its interaction with DNA. Acts by binding directly to the C-terminal domain of GyrB, which probably disrupts DNA binding by the gyrase. {ECO:0000255|HAMAP-Rule:MF_00649, ECO:0000269|PubMed:18586829}. EcoCyc product frame: EG12314-MONOMER. Genomic coordinates: 111649-111846. EcoCyc protein note: The YacG protein blocks DNA binding by CPLX0-2425, thereby inhibiting its function. YacG inhibits the supercoiling activity of DNA gyrase, as well as partially inhibiting its intrinsic ATPase activity. It does so via direct binding to the GyrB component of the gyrase holoenzyme and disrupting DNA binding by the enzyme. This inhibition is specific to gyrase, as neither topoisomerase I nor topoisomerase IV are affected by the presence of YacG . The structure of YacG has been analyzed via NMR. It appears to contain a classic zinc finger domain, including a tetrahedrally coordinated Zn2+ . Based on a deletion analysis, yacG appears to be dispensible for normal growth in minimal and rich medium . A yacL in-frame deletion strain has been constructed . Overexpression of yacG leads to growth inhibition and abnormally low levels of DNA supercoiling .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8H8|protein.P0A8H8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000351,ECOCYC:EG12314,GeneID:945630`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:111649-111846:-; feature_type=gene
