---
entity_id: "gene.b3470"
entity_type: "gene"
name: "tusA"
source_database: "NCBI RefSeq"
source_id: "gene-b3470"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3470"
  - "tusA"
---

# tusA

`gene.b3470`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3470`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tusA (gene.b3470) is a gene entity. It encodes tusA (protein.P0A890). Encoded protein function: FUNCTION: Sulfur carrier protein involved in sulfur trafficking in the cell. Part of a sulfur-relay system required for 2-thiolation during synthesis of 2-thiouridine of the modified wobble base 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) in tRNA (PubMed:16387657). Interacts with IscS and stimulates its cysteine desulfurase activity (PubMed:16387657, PubMed:23281480). Accepts an activated sulfur from IscS, which is then transferred to TusD, and thus determines the direction of sulfur flow from IscS to 2-thiouridine formation (PubMed:16387657). Also appears to be involved in sulfur transfer for the biosynthesis of molybdopterin (PubMed:23281480). Seems to affect the stability of sigma-S, particularly during the logarithmic growth phase (PubMed:9555915). {ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:23281480, ECO:0000269|PubMed:9555915}. EcoCyc product frame: EG12216-MONOMER. EcoCyc synonyms: yhhP, sirA. Genomic coordinates: 3608751-3608996. EcoCyc protein note: TusA has pleiotrophic roles in thiomodification of some tRNAs, sulfur transfer in molybdenum cofactor biosynthesis, general Fe-S cluster assembly, and iron homeostasis...

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A890|protein.P0A890]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011336,ECOCYC:EG12216,GeneID:947974`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3608751-3608996:-; feature_type=gene
