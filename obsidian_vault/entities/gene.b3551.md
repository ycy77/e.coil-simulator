---
entity_id: "gene.b3551"
entity_type: "gene"
name: "bisC"
source_database: "NCBI RefSeq"
source_id: "gene-b3551"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3551"
  - "bisC"
---

# bisC

`gene.b3551`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3551`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bisC (gene.b3551) is a gene entity. It encodes bisC (protein.P20099). Encoded protein function: FUNCTION: This enzyme may serve as a scavenger, allowing the cell to utilize biotin sulfoxide as a biotin source. It reduces a spontaneous oxidation product of biotin, D-biotin D-sulfoxide (BSO or BDS), back to biotin. Also exhibits methionine-(S)-sulfoxide (Met-S-SO) reductase activity, acting specifically on the (S) enantiomer in the free, but not the protein-bound form. It thus plays a role in assimilation of oxidized methionines. {ECO:0000269|PubMed:15601707, ECO:0000269|PubMed:2180922}. EcoCyc product frame: EG10124-MONOMER. Genomic coordinates: 3714061-3716394. EcoCyc protein note: BisC was first identified as a biotin sulfoxide reductase that reduces a spontaneous oxidation product of biotin, biotin-d-sulfoxide (BDS), back to biotin. The enzyme allows scavenging of BDS as a biotin source and may also protect the cell from oxidation damage . The other genes which were originally identified to be required for biotin sulfoxide reductase activity are likely involved in the biosynthesis and insertion of the molybdenum cofactor . A small, heat-stable, thioredoxin-like protein functions as a source for reducing equivalents and is required for biotin sulfoxide reductase activity...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P20099|protein.P20099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bisC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011597,ECOCYC:EG10124,GeneID:946915`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3714061-3716394:-; feature_type=gene
