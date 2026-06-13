---
entity_id: "gene.b2259"
entity_type: "gene"
name: "pmrD"
source_database: "NCBI RefSeq"
source_id: "gene-b2259"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2259"
  - "pmrD"
---

# pmrD

`gene.b2259`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2259`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pmrD (gene.b2259) is a gene entity. It encodes pmrD (protein.P37590). Encoded protein function: FUNCTION: Interacts with phosphorylated BasR protein to mediate transcriptional induction of BasR-activated genes to induce polymyxin resistance in some natural isolates. {ECO:0000269|PubMed:15569938}. EcoCyc product frame: G7172-MONOMER. Genomic coordinates: 2373272-2373538. EcoCyc protein note: PmrD is similar to the Salmonella enterica serovar Typhimurium PmrD, which confers resistance to polymyxin B when it is overexpressed ; in Salmonella, PmrD controls the activity of the PmrA-PmrB two-component system at a post-transcriptional level . E. coli PmrD is functional as a PhoP/PhoQ - PmrA/PmrB connector in Salmonella, but does not function in E. coli . The E. coli and Salmonella PmrD proteins have functionally diverged. In E. coli, PmrD is produced under conditions of low Mg2+ concentration in a PhoP-dependent manner; however, unlike in Salmonella, PmrD does not activate the PmrA-PmrB two-component system (known as PWY0-1482 "BasSR" in E. coli K-12) . This may explain why E. coli is unable to modify its LPS to become resistant to polymyxin B in medium containing low concentrations of Mg2+, such as LB . In addition, PmrA does not repress transcription of E. coli pmrD...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37590|protein.P37590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007468,ECOCYC:G7172,GeneID:945130`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2373272-2373538:-; feature_type=gene
