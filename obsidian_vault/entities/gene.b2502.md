---
entity_id: "gene.b2502"
entity_type: "gene"
name: "ppx"
source_database: "NCBI RefSeq"
source_id: "gene-b2502"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2502"
  - "ppx"
---

# ppx

`gene.b2502`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2502`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppx (gene.b2502) is a gene entity. It encodes ppx (protein.P0AFL6). Encoded protein function: FUNCTION: Degradation of inorganic polyphosphates (polyP). Releases orthophosphate processively from the ends of the polyP chain. Has a strong preference for long-chain polyphosphates and has only weak affinity for smaller size polyP of about 15 residues. {ECO:0000269|PubMed:16905100, ECO:0000269|PubMed:8380170, ECO:0000269|PubMed:9143103}. EcoCyc product frame: PPX-MONOMER. Genomic coordinates: 2625115-2626656. EcoCyc protein note: Exopolyphosphatase (PPX) degrades inorganic polyphosphates (polyP). It has a strong preference for long-chain polyphosphates; activity decreases with smaller size polyP of about 15 residues. PPX acts on the ends of the polyP chain, removing orthophosphate processively . Steady-state levels of polyP are dependent on the level of PPX in the cell . pppGpp and ppGpp strongly inhibit PPX activity while also acting as a substrate; however, GppA is the major source of pppGppase activity in the cell . PPX activity is redox-regulated; the enzyme is highly sensitive to inactivation by oxidation. Thus, oxidative stress conditions lead to accumulation of poly(P), which acts as a global chaperone...

## Biological Role

Repressed by lrp (protein.P0ACJ0), glaR (protein.P37338). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFL6|protein.P0AFL6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ppx; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008238,ECOCYC:EG11403,GeneID:946970`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2625115-2626656:+; feature_type=gene
