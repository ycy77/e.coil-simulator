---
entity_id: "gene.b2440"
entity_type: "gene"
name: "eutC"
source_database: "NCBI RefSeq"
source_id: "gene-b2440"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2440"
  - "eutC"
---

# eutC

`gene.b2440`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2440`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutC (gene.b2440) is a gene entity. It encodes eutC (protein.P19636). Encoded protein function: FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Ethanolamine ammonia-lyase (EAL) allows bacteria to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). Directly targeted to the BMC. May play a role in bacterial microcompartment (BMC) assembly or maintenance (By similarity). {ECO:0000250|UniProtKB:P19265, ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}. EcoCyc product frame: EUTC-MONOMER. Genomic coordinates: 2556410-2557297. EcoCyc protein note: An E. coli BW25113 mutant, which had the interrupting prophage between eutA and eutB removed, grows similarly to the E. coli K-12 strain W3110, which lacks the prophage in its eut transcription unit, when provided with ethanolamine (EA) as the sole nitrogen source . Further experiments to analyze ethanolamine utilization and the microcompartments were carried out in the E. coli W3110 strain...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19636|protein.P19636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008043,ECOCYC:EG50007,GeneID:946925`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2556410-2557297:-; feature_type=gene
