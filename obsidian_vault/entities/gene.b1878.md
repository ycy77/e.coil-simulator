---
entity_id: "gene.b1878"
entity_type: "gene"
name: "flhE"
source_database: "NCBI RefSeq"
source_id: "gene-b1878"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1878"
  - "flhE"
---

# flhE

`gene.b1878`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1878`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flhE (gene.b1878) is a gene entity. It encodes flhE (protein.P76297). Encoded protein function: FUNCTION: Not essential for flagellar formation and function. EcoCyc product frame: G7027-MONOMER. Genomic coordinates: 1962580-1962972. EcoCyc protein note: flhE forms an operon with flhB and flhA which encode type 3 flagellar export proteins . flhE mutants have a decreased cytoplasmic pH, grow poorly and form tiny colonies on LB agar, are impaired in swarming ability and undergo filament dependent cell lysis . Mutant phenotypes are dependent on filament assembly - flhE mutants do not show growth defects in fliK and flgL mutant backgrounds although they still have a decreased cytoplasmic pH . Acidification of the cytoplasm is indicative of a proton leak and thus FlhE may be involved in the regulation of proton flow through the type 3 secretion system The orthologous FlhE protein of Salmonella typhimurium is a periplasmic protein that co-purifies with flagellar basal bodies .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76297|protein.P76297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006270,ECOCYC:G7027,GeneID:946094`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1962580-1962972:-; feature_type=gene
