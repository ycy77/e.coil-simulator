---
entity_id: "gene.b0612"
entity_type: "gene"
name: "citT"
source_database: "NCBI RefSeq"
source_id: "gene-b0612"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0612"
  - "citT"
---

# citT

`gene.b0612`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0612`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citT (gene.b0612) is a gene entity. It encodes citT (protein.P0AE74). Encoded protein function: FUNCTION: Responsible for the uptake of citrate in exchange with the efflux of succinate, fumarate or tartrate. Has a relatively broad specificity for C(4)-dicarboxylates and tricarboxylates (PubMed:9696764). {ECO:0000269|PubMed:9696764}. EcoCyc product frame: B0612-MONOMER. EcoCyc synonyms: ybdS. Genomic coordinates: 645117-646580. EcoCyc protein note: CitT is a putative citrate/succinate antiporter, with the potential to support citrate uptake under anaerobic conditions. In aerobic conditions, E. coli cannot grow with citrate as a sole carbon and energy source due to a lack of transport (see ). Under anaerobic conditions, citrate can be utilised if an oxidizable cosubstrate is present such as glycerol or glucose. Expression of the cloned citT gene conferred the ability to utilise citrate in aerobic conditions. Whole cell transport assays indicated that CitT mediated exchange of citrate with citrate, succinate, tartrate or fumarate . Since succinate is the end product of citrate fermentation, it seems probable that CitT functions physiologically as a citrate/succinate exchanger in anaerobic conditions . Consistent with this supposition, CitT is a member of the DASS family of di- and tri-carboxylic acid transporters...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE74|protein.P0AE74]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002110,ECOCYC:G6338,GeneID:949070`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:645117-646580:-; feature_type=gene
