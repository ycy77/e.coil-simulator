---
entity_id: "gene.b0957"
entity_type: "gene"
name: "ompA"
source_database: "NCBI RefSeq"
source_id: "gene-b0957"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0957"
  - "ompA"
---

# ompA

`gene.b0957`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0957`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompA (gene.b0957) is a gene entity. It encodes ompA (protein.P0A910). Encoded protein function: FUNCTION: With TolR probably plays a role in maintaining the position of the peptidoglycan cell wall in the periplasm (Probable). Plays a role in resistance to environmental stress, and a role in outer membrane functionality and cell shape (PubMed:11906175, PubMed:361695). Non-covalently binds peptidoglycan (Probable) (PubMed:25135663). Acts as a porin with low permeability that allows slow penetration of small solutes (PubMed:1370823, PubMed:20004640, PubMed:21069910). A very abundant protein, there can be up to 210,000 OmpA molecules per cell (PubMed:24766808). Reconstitution in unilamellar lipid vesicles shows only about 3% of the protein is in an open conformation, which allows diffusion of L-arabinose at a rate comparable to that of OmpF porin; the pores interconvert very rarely (PubMed:7517935). Native and reconstituted protein forms ion channels with 2 conductance states of (50-80 pS) and (260-320 pS); the states are interconvertible in this study. Interconversion requires refolding of the periplasmic domain (PubMed:10636850). Small pores are converted into large pores by increasing temperature; in this model the C-terminal periplasmic domain forms 8 more beta sheets to form a larger pore (PubMed:15850404)...

## Biological Role

Repressed by micA (gene.b4442), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A910|protein.P0A910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ompA; function=+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=ompA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ompA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003240,ECOCYC:EG10669,GeneID:945571`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1019013-1020053:-; feature_type=gene
