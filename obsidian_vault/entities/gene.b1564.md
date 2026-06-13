---
entity_id: "gene.b1564"
entity_type: "gene"
name: "relB"
source_database: "NCBI RefSeq"
source_id: "gene-b1564"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1564"
  - "relB"
---

# relB

`gene.b1564`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1564`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

relB (gene.b1564) is a gene entity. It encodes relB (protein.P0C079). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Counteracts the effect of cognate toxin RelE via direct protein-protein interaction, preventing RelE from entering the ribosome A site and thus inhibiting its endoribonuclease activity. An autorepressor of relBE operon transcription. 2 RelB dimers bind to 2 operator sequences; DNA-binding and repression is stronger when complexed with toxin/corepressor RelE by conditional cooperativity (PubMed:18501926, PubMed:22981948). Increased transcription rate of relBE and activation of relE is consistent with a lower level of RelB in starved cells due to degradation of RelB by protease Lon. {ECO:0000269|PubMed:11274135, ECO:0000269|PubMed:11717402, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:18501926, ECO:0000269|PubMed:18532983, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:19747491, ECO:0000269|PubMed:22210768, ECO:0000269|PubMed:22981948, ECO:0000269|PubMed:9767574}.; FUNCTION: Seems to be a principal mediator of cell death in liquid media. {ECO:0000269|PubMed:19707553}. EcoCyc product frame: EG10836-MONOMER. EcoCyc synonyms: RC. Genomic coordinates: 1645633-1645872.

## Biological Role

Repressed by relB (protein.P0C079). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C079|protein.P0C079]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=relB; function=+
- `represses` <-- [[protein.P0C079|protein.P0C079]] `RegulonDB` `S` - regulator=RelB; target=relB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005224,ECOCYC:EG10836,GeneID:948308`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1645633-1645872:-; feature_type=gene
