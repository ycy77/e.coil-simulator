---
entity_id: "gene.b0467"
entity_type: "gene"
name: "priC"
source_database: "NCBI RefSeq"
source_id: "gene-b0467"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0467"
  - "priC"
---

# priC

`gene.b0467`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0467`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

priC (gene.b0467) is a gene entity. It encodes priC (protein.P23862). Encoded protein function: FUNCTION: Involved in the restart of stalled replication forks, which reloads the replicative helicase (DnaB) on sites other than the origin of replication (PubMed:10540288, PubMed:10835375, PubMed:22636770). Recognizes abandoned replication forks and remodels DNA single-stranded binding protein (SSB) on ssDNA to uncover a loading site for DnaB (PubMed:23629733, PubMed:27382050). There are several restart pathways, the PriA-PriC pathway is a minor restart pathway (PubMed:11532137, PubMed:22636770). Also part of the minor PriC-Rep pathway for restart of stalled replication forks, which has a different substrate specificity than PriA (PubMed:10835375, PubMed:17382604). priB and priC have redundant roles in the cell (PubMed:10540288). Stimulates the 3'-5' helicase activity of Rep helicase in vitro (PubMed:17382604). In vitro can load the DnaB replicative helicase from a DnaB-DnaC complex on an SSB-coated stalled replication fork with no leading- or lagging-strand (or with a gap between the leading strand and fork junction) in the absence of other primosome proteins (PriA, PriB or DnaT) (PubMed:15749022, PubMed:23629733, PubMed:27382050). Also part of the major restart pathway with PriA, PriB, DnaB, DnaT and DnaG primase (PubMed:8663105)...

## Biological Role

Activated by glaR (protein.P37338).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23862|protein.P23862]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=priC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001619,ECOCYC:EG10765,GeneID:945071`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:490285-490812:-; feature_type=gene
